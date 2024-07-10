# Blackjack Game

Welcome to the Blackjack game! This is a simple command-line implementation of the classic card game Blackjack. 

## How to Play

The objective of the game is to beat the dealer by having a hand value closest to 21 without exceeding it. Each card has a value:
- Number cards (2-10) have their face values.
- Face cards (Jack, Queen, King) are worth 10 points each.
- Aces can be worth either 1 or 11 points, depending on which value benefits the hand more.

### Game Rules

1. At the start of the game, both the player and the dealer are dealt two cards.
2. The player can see both their cards but only one of the dealer's cards.
3. The player can choose to:
    - `y`: Draw another card.
    - `n`: Pass and stop drawing cards.
4. The dealer will draw cards until their hand value is at least 17.
5. The game ends when either the player or the dealer busts (goes over 21) or both players choose to stand.

### Winning Conditions

- If the player's hand exceeds 21, they lose.
- If the dealer's hand exceeds 21, the player wins.
- If both hands are equal, it's a draw.
- If the player gets a Blackjack (an Ace and a 10-point card) on the initial deal, they win.
- If the dealer gets a Blackjack on the initial deal, the player loses.
- Otherwise, the hand closest to 21 without exceeding wins.

## Running the Game

To run the game, ensure you have Python installed. Then, execute the following command in your terminal:

```bash
python blackjack.py
