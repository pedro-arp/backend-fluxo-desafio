from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Teste para o endpoint de ingestão de dados
def test_ingest_data():
    with open("test/test_file.xlsx", "rb") as file:
        # Envia o arquivo para o endpoint
        response = client.post(
            "/lighting-data/upload",
            files={"file": ("test_file.xlsx", file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        )

        # Validação da resposta
        assert response.status_code == 200
        response_json = response.json()

        # Teste se a resposta contém todos os campos esperados (ajustados)
        assert "message" in response_json
        assert "duplicate_values_in_file" in response_json
        assert "duplicate_values_in_db" in response_json

        # Teste o conteúdo da mensagem
        assert "Inseridos" in response_json["message"]
        assert "registros com sucesso" in response_json["message"]

        # Teste o conteúdo dos valores duplicados, se aplicável
        assert isinstance(response_json["duplicate_values_in_file"], list)
        assert isinstance(response_json["duplicate_values_in_db"], list)

# Teste para o endpoint de consulta de dados
def test_get_lighting_posts():
    response = client.get("/lighting-posts?page=1&page_size=5")
    assert response.status_code == 200
    json_body = response.json()
    assert "posts" in json_body
    assert "total" in json_body
    assert len(json_body["posts"]) <= 5