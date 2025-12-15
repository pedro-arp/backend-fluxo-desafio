# Guia de Dependências do Projeto

## Arquivos de Requisitos

Este projeto utiliza uma estrutura organizada de arquivos de requisitos:

### `requirements.txt` - Dependências de Produção

Este arquivo contém **apenas** as dependências necessárias para executar a aplicação em produção.

**Instalação:**
```bash
pip install -r requirements.txt
```

**Dependências incluídas:**
- **fastapi** - Framework web para APIs
- **uvicorn[standard]** - Servidor ASGI com extras de performance (uvloop, httptools)
- **sqlalchemy** - ORM para banco de dados
- **alembic** - Migrations do banco de dados
- **pydantic** - Validação de dados
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **python-multipart** - Suporte para upload de arquivos no FastAPI
- **openpyxl** - Processamento de arquivos Excel (.xlsx)

### `requirements-dev.txt` - Dependências de Desenvolvimento

Este arquivo inclui todas as dependências de produção **mais** as ferramentas de desenvolvimento, teste e qualidade de código.

**Instalação:**
```bash
pip install -r requirements-dev.txt
```

**Dependências adicionais incluídas:**
- **httpx** - Cliente HTTP (necessário para FastAPI TestClient)
- **pytest** - Framework de testes
- **pytest-cov** - Relatórios de cobertura de código
- **pytest-asyncio** - Suporte a testes assíncronos
- **black** - Formatador de código
- **flake8** - Linter
- **isort** - Organização de imports
- **mypy** - Verificação de tipos

## Dependências Opcionais

### Adaptadores de Banco de Dados

Por padrão, o projeto usa **SQLite** (sem necessidade de dependências extras).

Para usar **PostgreSQL**, descomente a linha no `requirements.txt`:
```txt
psycopg2-binary==2.9.11
```

E configure a variável de ambiente:
```bash
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Mudanças Realizadas

### ✅ Dependências Removidas

As seguintes dependências foram **removidas** por não serem utilizadas no código:

1. **pandas** - Não há uso de pandas em nenhum arquivo Python do projeto
2. **anyio** - Instalado automaticamente como dependência do FastAPI/Starlette
3. **psycopg2-binary** - Movido para opcional (comentado), pois o projeto usa SQLite por padrão

### ✅ Melhorias Implementadas

1. **Organização Clara**: Requirements organizados em seções com comentários explicativos
2. **Separação de Ambientes**: Dependências de produção e desenvolvimento separadas
3. **Performance**: Adicionado `[standard]` ao uvicorn para melhor desempenho
4. **Documentação**: Comentários detalhados sobre cada dependência
5. **Flexibilidade**: Dependências opcionais claramente marcadas

## Recomendações de Uso

### Para Desenvolvimento Local

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar testes
pytest

# Executar com hot-reload
uvicorn app.main:app --reload
```

### Para Produção (Docker)

O `Dockerfile` já está configurado para usar `requirements.txt`:

```bash
docker-compose up --build
```

### Para CI/CD

Use `requirements-dev.txt` para executar testes e verificações de qualidade:

```yaml
# Exemplo para GitHub Actions
- name: Install dependencies
  run: pip install -r requirements-dev.txt

- name: Run tests
  run: pytest --cov=app

- name: Lint
  run: flake8 app/
```

## Verificação de Vulnerabilidades

Sempre verifique vulnerabilidades de segurança nas dependências:

```bash
# Instalar safety (se não estiver no requirements-dev.txt)
pip install safety

# Verificar vulnerabilidades
safety check

# Ou usar pip-audit
pip install pip-audit
pip-audit
```

## Atualização de Dependências

Para atualizar as dependências mantendo compatibilidade:

```bash
# Ver versões desatualizadas
pip list --outdated

# Atualizar uma dependência específica
pip install --upgrade <package-name>

# Gerar novo requirements.txt
pip freeze > requirements-temp.txt
# Revisar e mesclar manualmente
```

## Suporte

Para dúvidas ou problemas relacionados às dependências:
1. Verifique se está usando a versão correta do Python (3.12+)
2. Certifique-se de que o ambiente virtual está ativado
3. Limpe o cache do pip: `pip cache purge`
4. Reinstale: `pip install --force-reinstall -r requirements.txt`
