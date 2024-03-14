import random

MAX_LINES = 3  # global constant, it does not change
MAX_BET = 500
MIN_BET = 1

# creating our rows and columns for our slot machine
COLS = 3
ROWS = 3

# a dictionary to store the sysmbols that our machine will have

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_multiplier = {
    "A": 10,
    "B": 5,
    "C": 3,
    "D": 2
}


def check_winnings(columns, bet, lines, multiplier):
    winnings = 0
    winner_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            sysmbol_to_check = column[line]
            if symbol != sysmbol_to_check:
                break
        else:
            winnings = multiplier[symbol] * bet
            winner_lines.append(line + 1)
    return winnings, winner_lines


def slot_machine(rows, cols, symbols):
    all_symbols = []
    for key, value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)

    columns = []

    for _ in range(cols):
        column = []
        # copy of our list so that when we remove items it doesnt affect the orginal
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # we randomly choose our symbols
            value = random.choice(current_symbols)
            # so that we dont pick a value more times than we have
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def show_slot(columns):
    for row in range(len(columns[0])):
        for num, column in enumerate(columns):
            if num != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()


def deposit():
    # here we want to keep asking the user to enter an amount till
    # they enter a valid amount
    while True:
        amount = input("how much would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("amount must be a digit")
    return amount


def get_bet():

    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    "Invalid amount, a bet amount must be between R{} - R{}".format(MIN_BET, MAX_BET))
        else:
            print("amount must be a digit")
    return amount


def get_number_of_lines():

    while True:
        lines = input(
            f"Enter the number of lines you would like to be on (1- {MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            # this is to check if a number falls in btwn two numbers
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a  valid number of lines")
        else:
            print("lines must be a digit")
    return lines


def play(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        # i want to check if player balance is greater than their total amount they want to bet on
        if balance > total_bet:
            break
        else:
            print("You have insufficient balance, your current balance is R{}".format(
                balance))

    print("You have bet R{} on {} lines, your total bet is R{}".format(
        bet, lines, total_bet))
    game = slot_machine(ROWS, COLS, symbol_count)
    show_slot(game)
    results, winning_lines = check_winnings(
        game, bet, lines, symbol_multiplier)
    print(f"you have won R{results}")
    print("you have won on lines: ", *winning_lines)

    return results - total_bet


def main():
    balance = deposit()
    while True:
        print(f"your current balance is {balance}")
        spin = input("press enter to play or q to quit: ")
        if spin.lower() == "q":
            break
        balance += play(balance)
    print(f"you have R{balance} left")


main()
