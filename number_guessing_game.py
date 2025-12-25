import random
n = random.randint(1, 100)
a = -1
guesses = 0

while (a != n):
    a = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if a < n:
        print("higher number please")
    elif a > n:
        print("lower number please")
    else:
        print(f"Congratulations! You've guessed the number in {guesses} attempts.")


