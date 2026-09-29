# 📘 Assignment: Building REST APIs with the FastAPI Framework

## 🎯 Objective

Aprenda a construir uma API REST usando o framework FastAPI, definindo rotas, validando dados com modelos Pydantic e implementando operações CRUD em memória.

## 📝 Tasks

### 🛠️ Create a Health Check Endpoint

#### Descrição
Complete o endpoint `GET /health` no arquivo inicial para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Iniciar com `uvicorn starter-code:app --reload`
- Instalar as dependências com `pip install -r requirements.txt`
- Responder a `GET /health` com status HTTP `200`
- Retornar o JSON `{ "status": "ok" }`
- Exibir a documentação interativa em `/docs`


### 🛠️ Add a Validated Book Endpoint

#### Descrição
Use o modelo Pydantic `Book` fornecido no arquivo inicial e implemente `POST /books` para receber e validar dados de um livro.

#### Requisitos
O programa concluído deve:

- Usar os campos `title`, `author` e `year` do modelo `Book`
- Exigir `title` e `author` como textos não vazios
- Validar `year` como um número entre 0 e o ano atual
- Retornar o livro criado com status HTTP `201`
- Retornar um erro de validação automático para dados inválidos

Exemplo de requisição:

```json
{
  "title": "Dom Casmurro",
  "author": "Machado de Assis",
  "year": 1899
}
```


### 🛠️ Implement Book CRUD Operations

#### Descrição
Expanda a API para armazenar livros em memória e implemente as operações para listar, consultar, atualizar e remover livros.

#### Requisitos
O programa concluído deve:

- Atribuir um `id` único a cada livro criado
- Implementar `GET /books` para listar todos os livros
- Implementar `GET /books/{book_id}` para consultar um livro específico
- Implementar `PUT /books/{book_id}` para atualizar um livro existente
- Implementar `DELETE /books/{book_id}` e retornar status HTTP `204`
- Retornar status HTTP `404` quando o `book_id` não existir
- Manter os dados somente em memória, sem exigir um banco de dados