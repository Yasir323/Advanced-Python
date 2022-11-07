from typing import Union, Set, List
from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    """
    Nested Models
    """
    url: HttpUrl
    name: str


class Item(BaseModel):
    """
    The same way you can declare additional validation and metadata
    in path operation function parameters with Query, Path and Body,
    you can declare validation and metadata inside of Pydantic models
    using Pydantic's Field.
    """
    name: str
    description: Union[str, None] = Field(
        default=None, title='The description of the item', max_length=300
    )
    price: float = Field(gt=0, description='The price must be greater than 0')
    tax: Union[float, None] = None
    tags: Set[str] = []
    images: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]
