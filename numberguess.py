import random
import time

print("""
Number Guessing Game

-Computer will chose a random number between 1 and 1000.
-You got 10 guesses.
-Every time you guess, computer tells you higher or lower.
-If you can't find the number, computer wins.
-If you find the number, you win.
""")

random_number = random.randint(1,1000)
guesses = 10

while True:

    try:
        guess = int(input("Your guess:"))
    except:
        print("ERROR")
        continue

    if (guess < random_number):
        print("...")
        time.sleep(1)

        print("Say a higher number....")

        guesses -= 1
    elif (guess > random_number):
        print("...")
        time.sleep(1)

        print("Say a lower number....")

        guesses -= 1
    else:
        print("....")
        time.sleep(1)

        print("Congrats!\n Number is ",random_number)

        time.sleep(5)
        break
    if (guesses == 0):

        print("Your guess is over ...")
        print("Number is ",random_number)
        
        time.sleep(5)
        break
