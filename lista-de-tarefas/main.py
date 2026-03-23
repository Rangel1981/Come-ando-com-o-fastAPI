from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Minha API de Tarefas Profissional")

# Modelo de Dados (POO com Pydantic)
class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False

# Nosso "Banco de Dados" (Simulando persistência na memória)
banco_dados: List[Tarefa] = []

@app.get("/")
def home():
    return {"status": "Online", "mensagem": "PRA CIMA!"}

# --- CREATE (POST) com tratamento de ID duplicado ---
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
    # Verificando se o ID já existe para evitar conflitos
    for t in banco_dados:
        if t.id == tarefa.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Erro: Já existe uma tarefa com o ID {tarefa.id}."
            )
    
    banco_dados.append(tarefa)
    return {"mensagem": "Tarefa criada com sucesso!", "dados": tarefa}

# --- READ ALL (GET) ---
@app.get("/tarefas", response_model=List[Tarefa])
def listar_todas():
    return banco_dados

# --- READ BY ID (GET) com tratamento de erro 404 ---
@app.get("/tarefas/{tarefa_id}")
def buscar_por_id(tarefa_id: int):
    for tarefa in banco_dados:
        if tarefa.id == tarefa_id:
            return tarefa
    
    # Se não encontrar, lança a exceção 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"A tarefa {tarefa_id} não foi encontrada no servidor."
    )

# --- DELETE com tratamento de erro ---
@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for indice, tarefa in enumerate(banco_dados):
        if tarefa.id == tarefa_id:
            banco_dados.pop(indice)
            return {"mensagem": f"Tarefa {tarefa_id} removida com sucesso!"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não foi possível deletar: Tarefa inexistente."
    )