from fastapi import FastAPI, HTTPException
from gamelist.database import (
    add_game,
    get_all_games,
    get_game_by_id,
    delete_game,
)
from gamelist.schemas import GameCreate
from gamelist.models import Game

app = FastAPI()

@app.post("/games", response_model=Game)
def create_game(game: GameCreate):
    return db.add_game(game)

@app.get("/games", response_model=list[Game])
def list_games():
    return db.get_all_games()

@app.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int):
    game = db.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@app.delete("/games/{game_id}")
def delete_game(game_id: int):
    game = db.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete_game(game_id)
    return {"message": "Game deleted"}