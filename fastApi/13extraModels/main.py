from typing import Union, List, Dict
from fastapi import FastAPI
from utils import fake_save_user
from models import (
    UserIn,
    UserOut,
    UserInDB,
    PlaneItem,
    CarItem,
    Item
)

app = FastAPI()


@app.post('/user/', response_model=UserOut)
async def create_user(user_in: UserIn) -> UserInDB:
    user_saved = fake_save_user(user_in)
    return user_saved


"""
You can declare a response to be the Union of two types, that means,
that the response would be any of the two.
"""

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get('/items/{item_id}', response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


"""
Response Model can also be a list of time.
"""
items_ = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items_


"""
Response with arbitrary dict
"""


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
