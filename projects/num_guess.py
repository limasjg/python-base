# Number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a numver between {lowest_num} and {highest_num}")

while is_running:
    guess = input(f"Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Number is out range")
        elif guess < answer:
            print("Too low, try again!")
        elif guess > answer:
            print("Too high, try again!")
        else:
            print(f"Correct! the correct num is {answer} your try {guesses} times")
            is_running = False
    else:
        print("Invalid value")

# My poor tryed
# import random

# correct_num = random.randint(1, 100)
# attempt = 0
# while True:

#     guess = int(input("Enter a number (1 to 100): "))
#     if guess > correct_num:
#         print("Too High try again")
#         attempt += 1
#     elif guess < correct_num:
#         print("Too Low try again")
#         attempt += 1

#     elif guess == correct_num:
#         print(f" You Won! Correct num is {correct_num} after {attempt} attempts")
#         break

#     elif guess != guess.isdigit():
#         print("Try a digit idiot!")