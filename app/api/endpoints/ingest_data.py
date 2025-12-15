import re

from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.db.crud import bulk_insert_lighting_posts
from openpyxl import load_workbook
from datetime import datetime
from openpyxl.utils.datetime import from_excel

ingest_router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def process_date(value):
    if isinstance(value, int):  # Data no formato numérico do Excel
        return from_excel(value).date()
    elif isinstance(value, str):  # Data no formato string (ex: "12/05/2023")
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            return None
    return None

@ingest_router.post("/lighting-data/upload")
async def upload_lighting_data(file: UploadFile, db: Session = Depends(get_db)):
    duplicated_posts = []

    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Arquivo inválido. Apenas arquivos .xlsx são aceitos.")

    try:
        workbook = load_workbook(file.file)
        sheet = workbook.active
        posts_data = []
        for row_index, row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
            try:
                if any(record["id"] == row[5] for record in posts_data):
                    print(f"Registro duplicado encontrado no índice {row_index + 1}: ID {row[5]}.")
                    duplicated_posts.append({"id": str(row[5]),"Rua": row[0]})
                    continue

                installation_date = process_date(row[7])
                last_maintenance = process_date(row[8])

                post_data = {
                    "id": row[5],
                    "address": row[0],
                    "latitude": row[2],
                    "longitude": row[1],
                    "lamp_type": row[3],
                    "wattage": row[4],
                    "voltage": int(str(row[10]).replace("V", "")),
                    "needs_repair": row[9].lower() == "sim",
                    "last_maintenance": last_maintenance,
                    "installation_date": installation_date,
                    "hours_in_operation": row[9]
                }

                posts_data.append(post_data)
            except Exception as e:
                print(f"Erro ao processar linha {row_index + 1}: {e}")
                continue

        print(f"Dados processados para inserção: {posts_data}")

        if posts_data:
            try:
                total_inserted = bulk_insert_lighting_posts(db, posts_data)
            except Exception as e:
                print("Erro durante o Bulk Insert", e)
                raise HTTPException(status_code=404, detail="Erro durante o Bulk Insert")
        else:
            total_inserted = 0

        return {"message": f"Inseridos {total_inserted} registros com sucesso.",
                "duplicate_values": duplicated_posts
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))