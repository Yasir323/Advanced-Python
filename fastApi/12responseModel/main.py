from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = 10.5
    tags: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    """
    You might want to omit the default values that are not set from the
    result. Use the response_model_exclude_unset parameter for that.

    You can also use:
    response_model_exclude_defaults=True
    response_model_exclude_none=True
    """
    return items[item_id]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    """We can be more explicit as well."""
    return items[item_id]


@app.post('/user/', response_model=UserOut)
async def create_user(user: UserIn):
    """Since response model is UserOut, password is filtered out in the response."""
    return user
