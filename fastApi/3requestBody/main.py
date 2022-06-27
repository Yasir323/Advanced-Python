from typing import Optional
from models import Item
from fastapi import FastAPI

app = FastAPI()


@app.post('/items/{item_id}')
async def create_item(item: Item, item_id: int, q: Optional[str] = None):
    """Request Body + Path Parameters + Query Parameters"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    result =  {"item_id": item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result
