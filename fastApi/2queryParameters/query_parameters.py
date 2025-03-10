from typing import Optional
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {
        "item_name": "Foo"
    },
    {
        "item_name": "Bar"
    },
    {
        "item_name": "Baz"
    }
]


@app.get('/items')
async def read_item(offset: int = 0, limit: int = 10):
    """
    Open: http://127.0.0.1:8000/items?offset=1&limit=10
    """
    return fake_items_db[offset: offset + limit]


# Query parameter type conversion
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Multiple path query parameters
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str,
                         q: Optional[str], short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Required query parameters
@app.get("/required_items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
