# Handles creating a deck of cards, shuffling, and drawing cards.
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self) -> str:
        return f"{self.rank} or {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self) -> None:
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num = 1):
        return [self.cards.pop() for _ in range(num)]