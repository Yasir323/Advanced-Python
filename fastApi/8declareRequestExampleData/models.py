from typing import Union
from pydantic import BaseModel, Field


class Item(BaseModel):
    """
    When using Field() with Pydantic models, you can also declare
    extra info for the JSON Schema by passing any other arbitrary
    arguments to the function.
    """
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(default=None, example=3.2)

    class Config:
        """
        This extra info will be added as-is to the output JSON Schema
        for that model, and it will be used in the API docs.
        """
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
