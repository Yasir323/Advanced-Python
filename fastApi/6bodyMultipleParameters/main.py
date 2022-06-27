from typing import Union
from models import Item, User
from fastapi import FastAPI, Path, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
    user: Union[User, None] = None
):
    """
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
    user: Union[User, None] = None,
    importance: int = Body(gt=0)
):
    """
    The same way there is a Query and Path to define extra data
    for query and path parameters, FastAPI provides an equivalent
    Body.
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        },
        "importance": 5
    }
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    if importance:
        results.update({"importance": importance})
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    """
    If you want it to expect a JSON with a key item and inside of
    it the model contents, as it does when you declare extra body
    parameters, you can use the special Body parameter embed:
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        }
    }
    """
    results = {"item_id": item_id, "item": item}
    return results
