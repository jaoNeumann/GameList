from gamelist.models import Game
from gamelist.schemas import GameCreate

# Fake DB
games_db = []
next_id = 1

def add_game(game_data):
    global next_id
    game = Game(id=next_id, **game_data.dict())
    games_db.append(game)
    next_id += 1
    return game

def get_all_games():
    return games_db

def get_game_by_id(game_id: int):
    return next((game for game in games_db if game.id == game_id), None)

def delete_game(game_id: int):
    global games_db
    games_db = [game for game in games_db if game.id != game_id]
