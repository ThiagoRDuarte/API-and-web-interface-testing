# API e Interface Web

Este módulo implementa uma **API REST em Python** integrada a uma **interface web em Vue.js**, utilizando os dados tratados no **Teste 3**.  
O objetivo é demonstrar capacidade de construção de backend, frontend, integração com banco de dados, tomada de decisões técnicas e documentação.

---

## 📌 Visão Geral da Arquitetura

A aplicação foi dividida em dois módulos independentes:

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL  
- **Frontend**: Vue.js (SPA)

Essa separação facilita manutenção, escalabilidade e testes independentes.


---

## ⚙️ Backend – API REST

### 🔧 Tecnologias Utilizadas
- Python 3
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Uvicorn

---

### ▶️ Como executar o backend

- Acesse a pasta:
bash
cd API-and-web-interface-testing/backend

- Instale as dependencias:
python -m pip install --user -r requirements.txt

- Configure a conexão com o banco:
DATABASE_URL = "postgresql://postgres:SENHA@localhost:5432/teste_intuitive"

- Inicie a API:
python -m uvicorn main:app --reload

- API estará disponível em:
http://localhost:8000

---

### Rotas API

- Detalhes de uma Operadora
GET /api/operadoras?page=1&limit=10

- Listar Operadora
GET /api/operadoras/{cnpj}

- Despesas
GET /api/operadoras/{cnpj}/despesas

- Estatistícas
GET /api/estatisticas

## Trade-offs Técnicos

As decisões técnicas adotadas neste projeto consideraram o escopo do teste, o volume de dados e a necessidade de manter a solução simples, clara e de fácil manutenção.

No backend, foi escolhido o FastAPI devido à sua alta performance, tipagem forte com Pydantic e geração automática de documentação, reduzindo erros e facilitando a manutenção da API. Para a paginação, utilizou-se offset-based pagination, por ser simples e adequada ao volume de dados e à baixa frequência de atualizações.

Na rota de estatísticas, optou-se por consultas diretas ao banco de dados, priorizando consistência e simplicidade, já que o custo computacional é baixo e os dados não são atualizados em tempo real. A estrutura de resposta da API inclui dados e metadados, facilitando a implementação de paginação e controle de estado no frontend.

No frontend, a busca e o filtro foram implementados no servidor, evitando o carregamento excessivo de dados no cliente e melhorando a performance. O gerenciamento de estado foi realizado com Composables do Vue 3, suficientes para a complexidade da aplicação e sem o overhead de soluções globais. A performance da interface foi garantida com paginação no backend e tratamento explícito de estados de loading, erros e dados vazios, melhorando a experiência do usuário.

## Testes da API (Postman)

Local do arquivo:
API-and-web-interface-testing/postman/postman_collection.json

- Requisições Configuradas
- Respostas Reais
- Parametros e Urls Documentados;

## Autor
Thiago Ramos.






