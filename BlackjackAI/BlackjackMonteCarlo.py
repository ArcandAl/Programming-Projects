from cardDeck import Deck
import random

# return 0 if dealer win
# return 1 if player win
# return 2 if tie


def main():
    deck = Deck(6)
    cards = []
    decision = []
    playerHand = []
    dealerHand = []
    for i in range(2):
        playerHand.append(deck.deal())
        dealerHand.append(deck.deal())

    if scoreHand(playerHand) == 21:
        cards += [[scoreHand(playerHand), dealerHand[1][0]]]
        decision += ["Stay"]
        return 1, cards, decision

    # choose randomly to hit or stay for monte carlo
    for i in range(4):
        action = random.choice(["Hit", "Stay"])

        if action == "Hit":
            cards += [[scoreHand(playerHand), dealerHand[1][0]]]
            playerHand.append(deck.deal())
            if scoreHand(playerHand) > 21:
                # Player busted, should have stayed instead
                decision += ["Stay"]
                return 0, cards, decision
            elif scoreHand(playerHand) == 21:
                # player at 21, decision to hit correct
                decision += ["Hit"]
                return 1, cards, decision
            else:
                decision += ["Hit"]

        else:
            cards += [[scoreHand(playerHand), dealerHand[1][0]]]

            while scoreHand(dealerHand) <= 16:
                dealerHand.append(deck.deal())

            winner, decision = checkWin(dealerHand, playerHand, decision)
            return winner, cards, decision


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


# check to find winner of game
def checkWin(dealer, player, decision):
    dScore = scoreHand(dealer)
    pScore = scoreHand(player)

    # Dealer hand is higher but not over 21 or player busts
    if dScore > pScore and dScore <= 21 or pScore > 21:
        decision += ["Hit"]
        return 0, decision
    # Player hand is higher or Dealer has bust and Player has not
    elif pScore > dScore or pScore <= 21 and dScore > 21:
        decision += ["Stay"]
        return 1, decision
    else:
        decision += ["Stay"]
        return 2, decision


'''
if __name__ == '__main__':
    result, data, action = main()
    print(data)
    print(action)
'''
