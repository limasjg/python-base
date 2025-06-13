# Quiz Game

questions = ("How many elements are in the periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in the Earth's atmosphere?",
             "How many bones are in the adult human body?",
             "Which planet is the hottest in the solar system?")

options = (("A. 118", "B. 120", "C. 150", "D. 200"),
           ("A. Crocodile", "B. Elephant", "C. Blue Whale", "D. Ostrich"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 208", "C. 210", "D. 212"),
           ("A. Mercury", "B. Mars", "C. Venus", "D. Jupiter"))

answers = ("A", "D", "B", "A", "C")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! the right answer is {answers[question_number]} ")
    question_number += 1

print("-----------------------------------------------")
print("------------------ RESULT --------------------")
print("-----------------------------------------------")

print("Your guesses was:")
for guess in guesses:
    print(guess, end=" ")
print()

print("The right aswers was:")
for answer in answers:
    print(answer, end=" ")
print() 
total = int(score / len(questions) * 100)
print()
print(f"Your total was {total}%")