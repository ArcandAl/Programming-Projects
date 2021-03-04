import random


class Deck:

    def __init__(self, deckCount):
        self.suits = ["S", "H", "D", "C"]
        self.cardRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                         "Q", "K", "A"]
        self.cards = []
        self.buildDeck(deckCount)

    # creates a shoe with the specified number of decks and shuffles
    def buildDeck(self, numDeck):
        for i in range(numDeck):
            for j in self.suits:
                for k in self.cardRank:
                    self.cards.append(k+j)
        random.shuffle(self.cards)

    def getDeck(self):
        return self.cards

    # deals a card and removes it from the deck
    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
