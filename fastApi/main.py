from fastapi import FastAPI
from models import Item

app = FastAPI()


@app.get('/')
async def root():
    return {'message': "Hello World."}


@app.post("/item/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get('/item/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/users/me')
async def read_user_me():
    return {'user_name': "The current user."}


@app.get('/users/{user_name}')
async def read_user(user_name: str):
    return {'user_name': user_name}
