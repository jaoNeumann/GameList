from pydantic import BaseModel

class GameCreate(BaseModel):
    nome: str
    console: str
    genero: str
    ano: int
    imagem_url: str
