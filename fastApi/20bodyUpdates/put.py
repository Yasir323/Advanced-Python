from typing import List, Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    'foo': {'name': "Foo", 'price': 50.2},
    'bar': {'name': "Bar", 'description': "The Bartenders", 'price': 62, 'tax': 20.2},
    'baz': {'name': "Baz", 'description': None, 'price': 50.2, 'tax': 10.5, 'tags': []}
}


@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: str, item: Item):
    updated_item_encoded = jsonable_encoder(item)
    items[item_id] = updated_item_encoded
    return updated_item_encoded
