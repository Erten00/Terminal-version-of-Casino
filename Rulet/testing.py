import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox
import random

class RouletteGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Roulette")
        self.layout = QVBoxLayout()
        
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)
        
        self.color_button = QPushButton("Bet on Color")
        self.color_button.clicked.connect(self.get_color)
        self.layout.addWidget(self.color_button)
        
        self.number_button = QPushButton("Bet on Number")
        self.number_button.clicked.connect(self.get_number)
        self.layout.addWidget(self.number_button)
        
        self.oddity_button = QPushButton("Bet on Even/Odd")
        self.oddity_button.clicked.connect(self.get_even_odd)
        self.layout.addWidget(self.oddity_button)
        
        self.group_button = QPushButton("Bet on Group of 12")
        self.group_button.clicked.connect(self.get_group)
        self.layout.addWidget(self.group_button)
        
        self.half_button = QPushButton("Bet on Half")
        self.half_button.clicked.connect(self.get_half)
        self.layout.addWidget(self.half_button)
        
        self.column_button = QPushButton("Bet on Column")
        self.column_button.clicked.connect(self.get_column)
        self.layout.addWidget(self.column_button)
        
        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(self.get_result)
        self.layout.addWidget(self.continue_button)
        
        self.setLayout(self.layout)
        
        self.bets = []
        self.result = None
    
    def get_color(self):
        color_dialog = QSpinBox()
        color_dialog.setRange(1, 2)
        color_dialog.setPrefix("Choose color: ")
        color_dialog.setSuffix(" [1] for Red, [2] for Black")
        color_dialog.setSingleStep(1)
        color_dialog.valueChanged.connect(lambda value: setattr(self, 'color', value))
        color_dialog_amount = QSpinBox()
        color_dialog_amount.setPrefix("Enter bet amount: ")
        color_dialog_amount.setRange(1, 1000)
        color_dialog_amount.setSingleStep(10)
        color_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'color_amount', value))
        
        self.layout.addWidget(color_dialog)
        self.layout.addWidget(color_dialog_amount)
        
    def get_number(self):
        number_dialog = QSpinBox()
        number_dialog.setRange(0, 36)
        number_dialog.setPrefix("Enter the number you want to bet: ")
        number_dialog.setSingleStep(1)
        number_dialog.valueChanged.connect(lambda value: setattr(self, 'number', value))
        number_dialog_amount = QSpinBox()
        number_dialog_amount.setPrefix("Enter bet amount: ")
        number_dialog_amount.setRange(1, 1000)
        number_dialog_amount.setSingleStep(10)
        number_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'number_amount', value))
        
        self.layout.addWidget(number_dialog)
        self.layout.addWidget(number_dialog_amount)
        
    def get_even_odd(self):
        oddity_dialog = QSpinBox()
        oddity_dialog.setRange(1, 2)
        oddity_dialog.setPrefix("Enter [1] for Even, enter [2] for Odd: ")
        oddity_dialog.setSingleStep(1)
        oddity_dialog.valueChanged.connect(lambda value: setattr(self, 'oddity', value))
        oddity_dialog_amount = QSpinBox()
        oddity_dialog_amount.setPrefix("Enter bet amount: ")
        oddity_dialog_amount.setRange(1, 1000)
        oddity_dialog_amount.setSingleStep(10)
        oddity_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'oddity_amount', value))
        
        self.layout.addWidget(oddity_dialog)
        self.layout.addWidget(oddity_dialog_amount)
        
    def get_group(self):
        group_dialog = QSpinBox()
        group_dialog.setRange(1, 3)
        group_dialog.setPrefix("Enter the group index of 12's you want to bet: ")
        group_dialog.setSingleStep(1)
        group_dialog.valueChanged.connect(lambda value: setattr(self, 'group', value))
        group_dialog_amount = QSpinBox()
        group_dialog_amount.setPrefix("Enter bet amount: ")
        group_dialog_amount.setRange(1, 1000)
        group_dialog_amount.setSingleStep(10)
        group_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'group_amount', value))
        
        self.layout.addWidget(group_dialog)
        self.layout.addWidget(group_dialog_amount)
        
    def get_half(self):
        half_dialog = QSpinBox()
        half_dialog.setRange(1, 2)
        half_dialog.setPrefix("Choose the half you want to play: ")
        half_dialog.setSuffix(" [1] for 1 to 18, [2] for 19 to 36")
        half_dialog.setSingleStep(1)
        half_dialog.valueChanged.connect(lambda value: setattr(self, 'half', value))
        half_dialog_amount = QSpinBox()
        half_dialog_amount.setPrefix("Enter bet amount: ")
        half_dialog_amount.setRange(1, 1000)
        half_dialog_amount.setSingleStep(10)
        half_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'half_amount', value))
        
        self.layout.addWidget(half_dialog)
        self.layout.addWidget(half_dialog_amount)
        
    def get_column(self):
        column_dialog = QSpinBox()
        column_dialog.setRange(1, 3)
        column_dialog.setPrefix("Enter the index of the column you want to bet: ")
        column_dialog.setSingleStep(1)
        column_dialog.valueChanged.connect(lambda value: setattr(self, 'column', value))
        column_dialog_amount = QSpinBox()
        column_dialog_amount.setPrefix("Enter bet amount: ")
        column_dialog_amount.setRange(1, 1000)
        column_dialog_amount.setSingleStep(10)
        column_dialog_amount.valueChanged.connect(lambda value: setattr(self, 'column_amount', value))
        
        self.layout.addWidget(column_dialog)
        self.layout.addWidget(column_dialog_amount)
        
    def get_result(self):
        total_money = 0
        for bet in self.bets:
            if bet[0] == 'Color':
                total_money += self.check_color(bet[1], bet[2])
            elif bet[0] == 'Number':
                total_money += self.check_number(bet[1], bet[2])
            elif bet[0] == 'EvenOdd':
                total_money += self.check_oddity(bet[1], bet[2])
            elif bet[0] == 'Group':
                total_money += self.check_group(bet[1], bet[2])
            elif bet[0] == 'Half':
                total_money += self.check_half(bet[1], bet[2])
            elif bet[0] == 'Column':
                total_money += self.check_column(bet[1], bet[2])
        
        self.result = random.randrange(0, 37)
        
        result_text = f"Ball is on: {self.result}\n"
        if total_money > 0:
            result_text += f"Total earnings: {total_money} USD."
        else:
            result_text += "All bets are lost."
        
        self.result_label.setText(result_text)
        
    def check_color(self, color, amount):
        if (color == 1 and self.result % 2 == 1) or (color == 2 and self.result % 2 == 0):
            return amount
        return -amount
    
    def check_number(self, number, amount):
        if number == self.result:
            return amount * 36
        return -amount
    
    def check_oddity(self, oddity, amount):
        if (oddity == 1 and self.result % 2 == 0) or (oddity == 2 and self.result % 2 == 1):
            return amount
        return -amount
    
    def check_group(self, group, amount):
        if group == 1 and self.result >= 1 and self.result <= 12:
            return amount * 3
        elif group == 2 and self.result >= 13 and self.result <= 24:
            return amount * 3
        elif group == 3 and self.result >= 25 and self.result <= 36:
            return amount * 3
        return -amount
    
    def check_half(self, half, amount):
        if (half == 1 and self.result >= 1 and self.result <= 18) or (half == 2 and self.result >= 19 and self.result <= 36):
            return amount
        return -amount
    
    def check_column(self, column, amount):
        if column == 1 and self.result % 3 == 1:
            return amount * 3
        elif column == 2 and self.result % 3 == 2:
            return amount * 3
        elif column == 3 and self.result % 3 == 0:
            return amount * 3
        return -amount

if __name__ == "__main__":
    app = QApplication(sys.argv)
    roulette_game = RouletteGame()
    roulette_game.show()
    sys.exit(app.exec_())