from pydantic import BaseModel

class Game(BaseModel):
    id: int
    nome: str
    console: str
    genero: str
    ano: int
    imagem_url: str
