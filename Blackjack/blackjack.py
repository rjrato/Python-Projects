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
