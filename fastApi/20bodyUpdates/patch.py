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
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch('items/{item_id}', response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


# stored_item_data = items['baz']
# print(f'stored_item_data: {stored_item_data}')
# stored_item_model = Item(**stored_item_data)
# print(f'stored_item_model: {stored_item_model}')
# item = Item()
# item.name = 'baz'
# item.description = 'cool'
# update_data = item.dict(exclude_unset=True)
# print(f'update_data: {update_data}')
# updated_item = stored_item_model.copy(update=update_data)
# print(f'updated_item: {updated_item}')
# items['baz'] = jsonable_encoder(updated_item)
# print(items['baz'])
