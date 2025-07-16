import random
se_num = (random.randint(1, 100))

guess = None
attempts = 0

while guess != se_num:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < se_num:
     print("Too low, try again!")
    elif guess > se_num:
     print("Too high, try again!")
    else:
     print(f"correct ! you guessed in in {attempts} attempts.")