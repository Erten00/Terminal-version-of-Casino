import random

# Create two decks of cards
suits = ['❤️', '💎', '♣️', '♠️']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck1 = [(rank, suit) for suit in suits for rank in ranks]
deck2 = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the decks
random.shuffle(deck1)
random.shuffle(deck2)

# Deal the cards to the players
player1_hand = deck1[:4]
player2_hand = deck2[:4]

# Initialize inventories for both players
player1_inventory = []
player2_inventory = []

# Play the game
player1_score = 0
player2_score = 0
trick = 0
board = []

while True:
    trick += 1
    print(f"Trick {trick}")

    # Player 1's turn
    print("Player 1's turn:")
    print("Your hand:", player1_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card = player1_hand.pop(card_index)
    board.append(card)

    # Player 2's turn
    print("Player 2's turn:")
    print("Your hand:", player2_hand)
    card_index = int(input("Choose a card to play (enter the index): "))
    card_opponent = player2_hand.pop(card_index)
    board.append(card_opponent)

    print("\nBoard:", board)

    # Check for a match
    if card == card_opponent:
        if len(deck1) >= 2 and len(deck2) >= 2:
            player1_hand.extend([deck1.pop(0), deck2.pop(0)])
            player2_hand.extend([deck1.pop(0), deck2.pop(0)])
        elif len(deck1) > 0 and len(deck2) > 0:
            player1_hand.extend([deck1.pop(0), deck2.pop(0)])
            player2_hand.extend([deck1.pop(), deck2.pop()])
        elif len(deck1) == 0 and len(deck2) > 0:
            player2_hand.extend([deck2.pop(0), deck2.pop()])
        elif len(deck1) > 0 and len(deck2) == 0:
            player1_hand.extend([deck1.pop(0), deck1.pop()])
        else:
            break

    # Check if any player has no cards left
    if not player1_hand and not deck1:
        player1_score += len(board)
        board = []
    if not player2_hand and not deck2:
        player2_score += len(board)
        board = []

     # Check if both players have empty hands
    if not player1_hand and len(deck1) >= 4:
        player1_hand = deck1[:4]
        deck1 = deck1[4:]
    elif not player1_hand and len(deck1) > 0:
        player1_hand = deck1[:]
        deck1 = []
    if not player2_hand and len(deck2) >= 4:
        player2_hand = deck2[:4]
        deck2 = deck2[4:]
    elif not player2_hand and len(deck2) > 0:
        player2_hand = deck2[:]
        deck2 = []


    print()
    print("Scores:")
    print("Player 1:", player1_score)
    print("Player 2:", player2_score)
    print()
    print("Player 1's Inventory:", player1_inventory)
    print("Player 2's Inventory:", player2_inventory)
    print()

# Determine the winner of the game
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player2_score > player1_score:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")