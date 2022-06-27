from typing import Optional, Union
from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(default=None, min_length=3, max_length=10, regex='^fixedquery')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(default='fixedQuery', min_length=3, max_length=10, regex='^fixedquery')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(default=..., min_length=3, max_length=10, regex='^fixedquery')):
    """
    There's an alternative way to explicitly declare that a value is required.
    You can set the default parameter to the literal value ...
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=..., min_length=3, max_length=10, regex='^fixedquery')):
    """
    You can declare that a parameter can accept None, but that it's still required.
    This would force clients to send a value, even if the value is None."""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3, max_length=10, regex='^fixedquery')):
    """
    Use Pydantic's Required instead of Ellipsis
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Union[list[str], None] = Query(default=None)):
    """
    When you define a query parameter explicitly with Query you can
    also declare it to receive a list of values, or said in other way,
    to receive multiple values.

    http://localhost:8000/items/?q=foo&q=bar
    """
    query_items = {"q": q}
    return query_items


@app.get("/items/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    """
    Query parameter list / multiple values with defaults
    """
    query_items = {"q": q}
    return query_items


@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        alias="item-query",
        min_length=3,
    )
):
    """
    Adding more metadata.
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
