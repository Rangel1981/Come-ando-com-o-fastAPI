
# 🚀 Gerenciador de Tarefas - FastAPI (Hands-on)

Este projeto é uma API RESTful para gerenciamento de tarefas (To-Do List), desenvolvida para consolidar meus estudos em **Python**, **Programação Orientada a Objetos (POO)** e o framework **FastAPI**.

O foco principal foi aplicar boas práticas de desenvolvimento, como a tipagem de dados e o tratamento de exceções HTTP.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework moderno e de alta performance.
* **Pydantic**: Para validação de dados e criação de modelos (Schemas).
* **Uvicorn**: Servidor ASGI para rodar a aplicação.

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento, foquei em entregar um código com "cara de produção":

* **Validação de Dados**: Uso de classes Pydantic para garantir que a API receba apenas dados no formato correto.
* **Tratamento de Erros (HTTPException)**: Implementação de Status Codes adequados (404 para recursos não encontrados, 400 para requisições inválidas e 201 para criações).
* **CRUD Básico**: Operações de Criação, Leitura (Lista e ID único) e Deleção.
* **Documentação Automática**: Utilização do Swagger UI nativo do FastAPI para testes rápidos.

---
