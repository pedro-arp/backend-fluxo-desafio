# 🌟 Backend Fluxo Desafio 🚀

Este projeto consiste no desenvolvimento de uma API RESTful para gestão de dados de infraestrutura de iluminação pública. Utilizando **Python 3.13** e o framework **FastAPI**, a aplicação permite ingerir planilhas no formato `xlsx`, tratar e armazenar os dados em um banco de dados relacional, além de disponibilizar endpoints para consulta com suporte a filtros e paginação.

O objetivo deste desafio é demonstrar organização de código, boas práticas de desenvolvimento e competência técnica ao implementar os requisitos obrigatórios, com a possibilidade de adicionar diferenciais técnicos como containerização, testes automatizados e um design de API otimizado.

---

## 📂 Estrutura do Projeto

### Diretórios Principais
- **`alembic/`**: Gerenciamento de versões e migração do banco de dados.
- **`app/`**: Código principal da aplicação:
  - **`endpoints/`**: Endpoints da API.
  - **`db/`**: Configurações e lógica do banco de dados (CRUD, modelos, etc.).
- **`test/`**: Testes automatizados para validação da aplicação.

---

## 🛠️ Configuração e Instalação

### Pré-requisitos
- **Python 3.13**
- **pip** (Gerenciador de pacotes Python)
- Banco de dados SQLite (configuração padrão)

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/backend-fluxo-desafio.git
   cd backend-fluxo-desafio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   No Windows: venv\Scripts\activate # Linux: source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto:
   ```
   DATABASE_URL=sqlite:///./fluxo.db
   ```

---

## 📋 Rodando a Aplicação

### Aplicar Migrações com Alembic
1. Ative o ambiente virtual.
2. Aplique as migrações ao banco:
   ```bash
   alembic upgrade head
   ```

---

### Executar Localmente

1. Ative o ambiente virtual.
2. Rode o servidor **FastAPI**:
   ```bash
   uvicorn app.main:app --reload
   ```
   - Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ⚙️ Endpoints da API

### **`/lighting-data/upload`**
- **Método**: `POST`
- **Descrição**: Faz upload de um arquivo Excel com dados de iluminação pública.
- **Parâmetros**:
  - `file` (obrigatório): Arquivo `.xlsx`.
  - ![Exemplo Upload](https://github.com/user-attachments/assets/c951e2bf-e43a-45f6-99a0-dffa49bf8772)

#### **Resposta**:
- Registros únicos inseridos no banco.
- Registros duplicados não inseridos.

---

### **`/lighting-posts`**
- **Método**: `GET`
- **Descrição**: Consulta dados de iluminação pública.
- **Parâmetros**:
  - `page` (opcional): Número da página (default: 1).
  - `page_size` (opcional): Itens por página (default: 10).
  - `needs_repair` (opcional): Filtra por pontos que precisam de manutenção (`true`/`false`).
  - `lamp_type` (opcional): Filtra por tipo de lâmpada.

#### **Exemplo**:
```bash
curl --location 'http://localhost:8000/lighting-posts?page_size=30&page=1&needs_repair=true&lamp_type=LED'
```

#### **Resposta**:
- Lista de registros encontrados (paginada).

---

## 🚀 Docker

O projeto oferece suporte ao **Docker**.

### Configuração com Docker

1. Certifique-se de que o Docker está instalado.
2. Construa a imagem:
   ```bash
   docker-compose build
   ```
3. Inicie o container:
   ```bash
   docker-compose up
   ```
   - Acesse em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## 🧪 Testes Automatizados

Testes baseados no framework **pytest**.

### Rodar Testes
1. Ative o ambiente virtual.
2. Configure corretamente o interpretador Python.
3. Execute os testes:
   ```bash
   pytest test/test_endpoints.py
   ```

---

## 💡 Tecnologias Utilizadas

- **FastAPI**: Desenvolvimento de APIs rápidas e intuitivas.
- **SQLAlchemy**: Manipulação do banco de dados (ORM).
- **OpenPyXL**: Leitura e manipulação de arquivos Excel.
- **Pytest**: Framework de testes automatizados.
- **Alembic**: Migração e versionamento do banco.
- **Docker**: Containerização da aplicação.

---

## ✍️ Autor 
Desenvolvido com 💻 por **Pedro Pereira**.
