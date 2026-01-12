# Desafio Técnico Backend | Fluxo

## 1. Introdução

Na **Fluxo**, valorizamos a capacidade de transformar dados brutos em informação acionável. Este desafio simula uma situação real onde precisamos ingerir dados legados de infraestrutura urbana (iluminação pública) e disponibilizá-los para nossa plataforma de gestão inteligente.

O objetivo não é apenas "fazer funcionar", mas demonstrar organização, conhecimento das ferramentas e aderência às boas práticas de desenvolvimento moderno em Python.

## 2. O Objetivo

Você deve desenvolver uma API RESTful utilizando **Python 3.13** e o framework **FastAPI**. A aplicação deve ser capaz de ler um arquivo de planilha (dados de postes de iluminação), processar e sanitar as informações, salvá-las em um banco de dados relacional e expor esses dados através de endpoints otimizados.

## 3. Requisitos Técnicos Obrigatórios (MVP)

  * **Linguagem:** Python 3.13.
  * **Framework:** FastAPI.
  * **Banco de Dados:** Relacional (PostgreSQL ou SQLite), uso de ORM SQLAlchemy e versionamento com Alembic é mandatório.
  * **Validação de Dados:** Pydantic.
  * **Versionamento:** O código deve estar hospedado em um repositório público (GitHub ou GitLab).

## 4. Escopo Funcional

### A. Ingestão de Dados

Desenvolver um endpoint que receba o arquivo `Simulação Estado Atual de Iluminação.xlsx`.

  * O sistema deve ler o arquivo e inserir os registros no banco de dados.
  * **Tratamento de Dados Obrigatório:**
      * Converter as colunas de data para objetos `date` ou `datetime` nativos.
      * Converter a coluna "Precisa de Manutenção" (Sim/Não) para Booleano (`True`/`False`).
      * Limpar a coluna "Voltagem" para armazenar apenas o número inteiro (ex: `127` ao invés de `127V`), ou validar se o sufixo existe.

### B. Consulta de Dados

Desenvolver um endpoint para listar os pontos de iluminação cadastrados.

  * **Paginação:** O endpoint deve aceitar parâmetros para controlar a paginação dos resultados (ex: `page` e `page_size` ou `skip` e `limit`).
  * **Filtros:** Deve ser possível filtrar por:
      * Tipo de lâmpada (ex: LED, Vapor de Sódio).
      * Status de manutenção (apenas os que precisam de manutenção).
  * **Estrutura de Resposta:** A resposta JSON deve ser bem estruturada. As informações geográficas devem estar agrupadas. Exemplo de formato desejado:

```json
{
  "id": "P-15724",
  "address": "Rua Imperial, 1837 - Rio de Janeiro - RJ",
  "location": {
    "lat": -22.847185,
    "long": -43.359986
  },
  "equipment": {
    "type": "Vapor Metálico",
    "wattage": 400,
    "voltage": 127
  },
  "maintenance": {
    "needs_repair": false,
    "last_maintenance": "2020-12-12"
  }
}
```

## 5. Diferenciais

Se você quiser demonstrar profundidade técnica, aqui estão algumas sugestões que valorizamos muito (não são obrigatórios, mas contam pontos):

1.  **Containerização:** Entregar o projeto com `Dockerfile` e `docker-compose` para rodar a aplicação e o banco com um único comando.
2.  **Testes Automatizados:** Implementação de testes unitários ou de integração (Pytest).
3.  **Arquitetura:** Organização do projeto seguindo padrões limpos (ex: separação de Routers, Controllers/Services, Schemas e Models).
4.  **Performance:** Uso de inserção em massa (*bulk insert*) para o upload da planilha, visando performance.
5.  **Tratamento de Erros:** Retornos de erro HTTP adequados e mensagens claras caso a planilha esteja fora do padrão.

## 6. O Dataset

Você receberá o arquivo `Simulação Estado Atual de Iluminação.xlsx` contendo as colunas:

  * `Rua`, `Longitude`, `Latitude`
  * `Tipo de Lampada`, `Potencia em W`, `Voltagem`
  * `Registro` (Identificador único do poste)
  * `Data da Instalação`, `Ultima Manutenção`
  * `Horas em Operação`
  * `Precisa de Manutenção`

## 7. Critérios de Avaliação

O seu teste será avaliado com base em:

1.  **Qualidade do Código:** Clareza, legibilidade e PEP8.
2.  **Design da API:** Uso correto dos verbos HTTP, status codes e estrutura dos recursos.
3.  **Modelagem de Dados:** Como você estruturou o banco para atender aos requisitos.
4.  **Documentação:** Um arquivo `README.md` explicando como instalar e rodar o projeto é essencial.

## 8. Entrega

Envie o link do repositório publico para a **Fluxo** até a data informada e para os e-mails indicadas no canal pelo qual recebeu este desafio.
