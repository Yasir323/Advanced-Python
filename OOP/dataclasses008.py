"""
Comparing cards:

You can also give parameters to the @dataclass() decorator in parentheses. The following parameters are supported:

init: Add .__init__() method? (Default is True.)
repr: Add .__repr__() method? (Default is True.)
eq: Add .__eq__() method? (Default is True.)
order: Add ordering methods? (Default is False.)
unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
frozen: If True, assigning to fields raise an exception. (Default is False.)
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.suit}{self.rank}"


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self) -> str:
        cards = ', '.join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts)
"""
It turns out that data classes compare objects as if they were 
tuples of their fields. In other words, a Queen is higher than 
an Ace because 'Q' comes after 'A' in the alphabet.

Instead, we need to define some kind of sort index that uses 
the order of RANKS and SUITS. Something like this:
"""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
card = PlayingCard('Q', '♡')
RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit)

"""
For PlayingCard to use this sort index for comparisons, we need 
to add a field .sort_index to the class. However, this field 
should be calculated from the other fields .rank and .suit 
automatically. This is exactly what the special method .__post_init__() is for. It allows for special processing after the regular .__init__() method is called:
"""


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
print(ace_of_spades > queen_of_hearts)
