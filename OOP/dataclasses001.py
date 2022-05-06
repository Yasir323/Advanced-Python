from dataclasses import dataclass
from typing import Union


@dataclass
class Card:
    rank: Union[str, int]
    suit: str


queen_of_hearts = Card('Q', 'Hearts')
print(queen_of_hearts)
print(queen_of_hearts.rank)
