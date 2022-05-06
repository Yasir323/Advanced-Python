"""
Immutable data classes
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = Position('Oslo', 10.8, 59.9)
try:
    pos.name = 'Stockholm'
except:
    print("Cannot assign to field 'name'.")


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]



"""
Even though both ImmutableCard and ImmutableDeck are immutable,
the list holding cards is not. You can therefore still change
the cards in the deck:
"""
queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)
deck.cards[0] = ImmutableCard('7', '♢')
print(deck)
