# Slot Machine Program
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐":
            return bet * 20
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
    return 0
        
def main():
    balance = 100

    print("----------------------------")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("----------------------------")

    while balance > 0:
      print(f"Current balance: ${balance}")

      bet = input("Enter your bet amount: ")


      if not bet.isdigit():
          print("Invalid bet amount.")
          continue
      
      bet = int(bet)


      if bet > balance:
          print("Insufficient balance.")
          continue
      
      if bet <= 0:
          print("Bet amount must be greater than zero.")
          continue
      
      balance -= bet

      row =spin_row()
      print("Spinning...\n")
      print_row(row)
      print()

      payout = get_payout(row, bet)

      if payout > 0:
          print(f"Congratulations! You won ${payout}!")
          balance += payout
      else:
          print("Better luck next time!")

      play_again = input("Do you want to play again? (y/n): ").lower()
      if play_again != "y":
          break
    print(f"Thank you for playing! Your final balance is: ${balance}")

if __name__ == "__main__":
    main()

