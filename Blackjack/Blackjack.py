import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
import random
import Cards


class BlackjackGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blackjack")
        self.cards = Cards.cards
        self.cards_value = Cards.cards_value
        self.money = 100
        self.money_won = 0
        self.money_lost = 0
        self.player_sum = [0]
        self.dealer_sum = [0]
        self.player_cards = []
        self.dealer_cards = []

        self.initUI()

    def initUI(self):
        self.label_money = QLabel("Money: 100")
        self.label_bet = QLabel("Bet: 0")
        self.label_player = QLabel("Player's Hand:")
        self.label_sum = QLabel("Sum: 0")
        self.label_dealer = QLabel("Dealer's Hand:")

        self.line_edit_bet = QLineEdit()
        self.line_edit_bet.setPlaceholderText("Enter bet amount")

        self.button_start = QPushButton("Start")
        self.button_start.clicked.connect(self.startGame)

        self.button_hit = QPushButton("Hit")
        self.button_hit.clicked.connect(self.hit)

        self.button_stand = QPushButton("Stand")
        self.button_stand.clicked.connect(self.stand)
        self.button_stand.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label_money)
        layout.addWidget(self.label_bet)
        layout.addWidget(self.line_edit_bet)
        layout.addWidget(self.label_player)
        layout.addWidget(self.label_sum)
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_hit)
        layout.addWidget(self.button_stand)
        layout.addWidget(self.label_dealer)

        self.setLayout(layout)

    def startGame(self):
        bet_amount = self.line_edit_bet.text()
        if bet_amount.isdigit():
            bet = int(bet_amount)
            if bet <= self.money:
                self.money -= bet
                self.label_money.setText(f"Money: {self.money}")
                self.label_bet.setText(f"Bet: {bet}")
                self.button_start.setEnabled(False)
                self.button_hit.setEnabled(True)
                self.button_stand.setEnabled(True)

                self.player_cards = []
                self.dealer_cards = []
                self.player_sum[0] = 0
                self.dealer_sum[0] = 0

                self.drawCard(self.player_cards, self.player_sum)
                self.drawCard(self.player_cards, self.player_sum)
                self.drawCard(self.dealer_cards, self.dealer_sum)
                self.drawCard(self.dealer_cards, self.dealer_sum)

                self.label_player.setText(f"Player's Hand: {', '.join(self.player_cards)}")
                self.label_dealer.setText(f"Dealer's Hand: {self.dealer_cards[0]}, ?")
                self.label_sum.setText(f"Sum: {self.player_sum[0]}")

    def hit(self):
        self.drawCard(self.player_cards, self.player_sum)
        self.label_player.setText(f"Player's Hand: {', '.join(self.player_cards)}")
        self.label_sum.setText(f"Sum: {self.player_sum[0]}")

        if self.player_sum[0] > 21:
            self.endGame("Crash")
            self.button_hit.setEnabled(False)

    def stand(self):
        while self.dealer_sum[0] < 17:
            self.drawCard(self.dealer_cards, self.dealer_sum)

        self.label_dealer.setText(f"Dealer's Hand: {', '.join(self.dealer_cards)}")

        if self.dealer_sum[0] > 21 or self.player_sum[0] > self.dealer_sum[0]:
            self.endGame("Win")
        elif self.player_sum[0] == self.dealer_sum[0]:
            self.endGame("Tie")
        else:
            self.endGame("Lose")

    def drawCard(self, hand, hand_sum):
        card_index = random.randint(0, len(self.cards) - 1)
        card = self.cards[card_index]
        card_value = self.cards_value[card_index]
        hand.append(card)

        if card_value == 11 and hand_sum[0] + card_value > 21:
            card_value = 1

        hand_sum[0] += card_value

        # Update the dealer_sum attribute when drawing cards for the dealer
        if hand is self.dealer_cards:
            self.dealer_sum[0] = hand_sum[0]

        # Update the player_sum attribute when drawing cards for the player
        if hand is self.player_cards:
            self.player_sum[0] = hand_sum[0]

    def endGame(self, result):
        self.button_hit.setEnabled(False)
        self.button_stand.setEnabled(False)
        self.button_start.setEnabled(True)

        if result == "Win":
            self.money += 200
        elif result == "Tie":
            self.money += 10

        self.label_money.setText(f"Money: {self.money}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = BlackjackGame()
    game.show()
    sys.exit(app.exec_())