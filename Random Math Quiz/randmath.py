import random

c = 1
def mathquiz(t, d):
    # Keeps track of what question user is on
    global c
    # Checks if not out of questions
    if t != 0:
        # Assigns usable operations based on difficulty, then gets a random operator
        ezops, medops, hardops = ['+', '-'], ['+', '-', '*'], ['+', '-', '*', '^']
        op = ezops if d == 1 else medops if d == 2 else hardops
        rop = random.choice(op)
        # Gets random numbers based on difficulty and operator
        n1 = random.randint(1,25) if rop == '^' else random.randint(1,10) if d == 1 else random.randint(1,100) if d == 2 else random.randint(1,500)
        n2 = random.randint(1,5) if rop == '^' else random.randint(1,10) if rop == '*' and d == 2 else random.randint(1,25) if rop == '*' and d == 3 else random.randint(1,10) if d == 1 else random.randint(1,100) if d == 2 else random.randint(1,500)
        # Calculates answer
        ans = (n1 + n2) if rop == "+" else (n1 - n2) if rop == "-" else (n1 * n2) if rop == "*" else (n1 ** n2)
        # Takes user answer and compares to actual, if correct continues quiz
        guess = int(input("\nQuestion {}\nWhat is {} {} {}: ".format(c, n1,rop,n2)))
        if guess == ans:
            print("Correct!")
            t -= 1
            c += 1
            return mathquiz(t, d)
        # If incorrect answer, returns answer and asks if should make another quiz
        c = 1
        again = input("\nIncorrect, the answer was {}! The Random Math Quiz has been failed!\nTry again? (Y/N): ".format(ans))
        mathquiz(turns, dif) if again[0].upper() == "Y" else quit()
    # If all correct, congratulates user and asks if should make another quiz
    c = 1
    again = input("\nCongratulations! You have passed The Random Math Quiz!\nTry again? (Y/N): ")
    mathquiz(turns, dif) if again[0].upper() == "Y" else quit()
# Takes in amount of turns and difficulty for quiz
turns = int(input("Welcome to The Random Math Quiz!\nAnswer all questions correctly to pass!\nEnter number of questions: "))
dif = int(input("Enter difficulty range (1 to 3): "))
# Checks if the amount of turns are above 0 and the range is within bounds, initializes math quiz
if turns <= 0:
    print("Turns must be a number above zero!")
if dif > 3 or dif < 1:
    print("Difficulty must be in the number range 1 to 3!")
t, d = turns, dif
mathquiz(t, d)