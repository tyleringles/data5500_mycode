import random
from deckOfCards import * 

print("Welcome to Blackjack!\n")


def calc_score(hand):
    score = 0
    aces = 0

    for card in hand:
        score += card.num
        if card.face == "Ace":
            aces += 1


    while score > 21 and aces:
        score -= 10  #
        aces -= 1

    return score


while True:
    
    deck = deckOfCards()
    print("deck before shuffled:")
    deck.print_deck()
    deck.shuffle_deck()
    print("\ndeck after shuffled:")
    deck.print_deck()

   
    player_hand = [deck.get_card(), deck.get_card()]
    dealer_hand = [deck.get_card(), deck.get_card()]


    print("\nYour cards:")
    for card in player_hand:
        print(card)
    print(f"Your total score is: {calc_score(player_hand)}")


    while True:
        move = input("Would you like a hit? (y/n): ").lower()
        if move == 'y':
            player_hand.append(deck.get_card())
            print("\nYou got:")
            print(player_hand[-1])
            print(f"Your total score is: {calc_score(player_hand)}")
            if calc_score(player_hand) > 21:
                print("You bust! You lose!")
                break
        elif move == 'n':
            print("\nYou stand with a score of:", calc_score(player_hand))
            break
        else:
            print("Invalid input. Please enter 'y' for hit or 'n' for stand.")

    