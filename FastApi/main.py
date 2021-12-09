from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins= [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

pessoadb = []

class Pessoa(BaseModel):
    pessoa_id: int
    nome: str
    rg: str
    idade: int
    sexo: str
 

@app.get("/")
def read_root():
    return {"home": "Home Page"}

@app.get("/pessoa")
def read_pessoa():
    return pessoadb

@app.get("/pessoa/{pessoa_id}")
def get_pessoa(pessoa_id: int):
    for pessoa in pessoadb:
        if(pessoa.get('pessoa_id') == pessoa_id):
            return pessoa
    return {"message": "Pessoa não encontrada"}

@app.post("/pessoa")
def add_pessoa(pessoa: Pessoa):
    pessoadb.append(pessoa.dict())
    return pessoadb[-1]

@app.put("/pessoa/{pessoa_id}")
def update_pessoa(pessoa_id: int, pessoa: Pessoa):
    for p in pessoadb:
        if(p.get('pessoa_id') == pessoa_id):
            p["pessoa_id"] = pessoa.pessoa_id
            p["nome"] = pessoa.nome
            p["rg"] = pessoa.rg
            p["idade"] = pessoa.idade
            p["sexo"] = pessoa.sexo
    return {"message": "Pessoa atualizada com sucesso!"}

@app.delete("/pessoa/{pessoa_id}")
def delete_pessoa(pessoa_id: int):
    count = 0
    for pessoa in pessoadb:
        if(pessoa.get('pessoa_id') == pessoa_id):
            break
        count += 1
    try:
        pessoadb.pop(count)
        return {"message": "Pessoa deletada com sucesso!"}
    except:
        return {"message": "Pessoa não encontrada"}
    
