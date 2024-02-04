from art import logo
import random
import os

os.system("cls")


def clear():
    os.system("cls")


def play():
    play_game = input("Do you want to play a BlackJack game? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        clear()
        print(logo)
        blackjack()


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = cards[random.randint(0, 10)]
    return random_card


def get_card():
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    return get_another_card


def blackjack():
    player_hand = [deal_card(), deal_card()]
    player_score = sum(player_hand)

    dealer_hand = [deal_card(), deal_card()]
    dealer_score = sum(dealer_hand)

    while dealer_score < 17:
        dealer_new_card = deal_card()
        dealer_hand.append(dealer_new_card)
        dealer_score += dealer_new_card

    print(f"  Your cards: {player_hand}, current score: {player_score}")
    print(f"  Dealer first card: {dealer_hand[0]}")

    another_card = True

    while another_card:

     if get_card() == 'y':
       new_card = deal_card()
       player_hand.append(new_card)
       player_score += new_card
       print(f"  Your cards: {player_hand}, current score: {player_score}")
       print(f"  Dealer first card: {dealer_hand[0]}")

       if player_score > 21:
          another_card = False
          result(player_score, player_hand, dealer_hand, dealer_score)

     else:

       another_card = False

       result(player_score, player_hand, dealer_hand, dealer_score)

      

def result(player_score, player_hand, dealer_hand, dealer_score):

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer final hand: {dealer_hand}, final score: {dealer_score}")
  
    if dealer_score > 21:
        print("Opponent went over. You win! 😁")
        play()
    elif player_score > 21:
        print("You went over. You lose 😤")
        play()
    elif player_score > 21 and dealer_score > 21:
        print("No one win 🙃")
    elif sum(player_hand) == 21 and len(player_hand) == 2:
        print("It's a Blackjack! You win 😎!")
        play()
    elif sum(dealer_hand) == 21 and len(dealer_hand) == 2:
        print("Dealer got a Blackjack! You lose 😱!")
        play()
    elif player_score == dealer_score:
        print("Draw 🙃")
        play()   
    elif player_score > dealer_score:
       print("You win! 😁")  
       play() 
    else:
       print("You lose! 😤")
       play()

play()

'''
chat-gpt version

import random

# Define the card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculate the score of a given hand."""
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def check_blackjack(hand):
    """Check for a blackjack."""
    return sum(hand) == 21 and len(hand) == 2

def compare_scores(player_score, dealer_score):
    """Compare player's and dealer's scores and determine the result."""
    if player_score > 21:
        return "You went over 21. You lose."
    elif dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif player_score == dealer_score:
        return "It's a draw."
    elif player_score == 21:
        return "You have a Blackjack! You win!"
    elif dealer_score == 21:
        return "Dealer has a Blackjack. You lose."
    elif player_score > dealer_score:
        return "You have a higher score. You win!"
    else:
        return "Dealer has a higher score. You lose."

def play_blackjack():
    """Play a game of Blackjack."""
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your hand: {player_hand}, score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' for another card, 'n' to pass: ")
            if another_card == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 21 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

# Main Game Loop
while input("Do you want to play Blackjack? (y/n): ") == "y":
    play_blackjack()
'''