from cardDeck import Deck

# return 0 if dealer win
# return 1 if player win
# return 2 if tie


def main():
    deck = Deck(6)
    playerHand = []
    dealerHand = []
    for i in range(2):
        playerHand.append(deck.deal())
        dealerHand.append(deck.deal())

    if scoreHand(playerHand) == 21:
        return 1

    while (scoreHand(playerHand) < 12 or scoreHand(playerHand) > 11
           and scoreHand(playerHand) < 17
           and scoreHand(dealerHand[1][0]) >= 7):
        playerHand.append(deck.deal())

    # check if player busts
    if scoreHand(playerHand) > 21:
        return 0

    while scoreHand(dealerHand) <= 16:
        dealerHand.append(deck.deal())

    winner = checkWin(dealerHand, playerHand)
    return winner


# scores the specified hand of cards
def scoreHand(hand):
    score1 = 0
    score2 = 0
    ace = False
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "J": 10, "Q": 10, "K": 10}

    for card in hand:
        if card[0] == "1":
            score1 += 10
        elif card[0] == "A":
            ace = True
        else:
            score1 += values[card[0]]

    if ace:
        score2 = score1 + 11
        score1 += 1

    if score2 != 0 and score2 <= 21:
        return score2
    else:
        return score1


def checkWin(dealer, player):
    dScore = scoreHand(dealer)
    pScore = scoreHand(player)

    # Dealer hand is higher but not over 21
    if dScore > pScore and dScore <= 21 or pScore > 21:
        # print("Dealer Wins")
        return 0
    # Player hand is higher or Dealer has bust and Player has not
    elif pScore > dScore or pScore <= 21 and dScore > 21:
        return 1
    else:
        return 2
