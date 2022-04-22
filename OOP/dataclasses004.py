from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
"""
For fun, the four different suits are specified using their 
Unicode symbols.
"""


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


make_french_deck()
print(make_french_deck()[:5])

"""
@dataclass
class Deck:  # Will NOT work
    cards: List[PlayingCard] = make_french_deck()

Don’t do this! This introduces one of the most common 
anti-patterns in Python: using mutable default arguments. 
The problem is that all instances of Deck will use the same 
list object as the default value of the .cards property. 
This means that if, say, one card is removed from one Deck, 
then it disappears from all other instances of Deck as well. 
Actually, data classes try to prevent you from doing this, 
and the code above will raise a ValueError.
"""
