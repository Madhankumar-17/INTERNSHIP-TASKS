import random
def check_guess(secret,guess):
    if guess == secret:
        return "Correct!" 
    elif guess < secret:
        return "Too low! Try higher"
    else:
        return "Too high! Try lower"
secret = random.randint(1, 100)
for attempt in range (3):
    guess = int(input("Guess a number between 1 and 100: "))
    result = check_guess(secret, guess)
    print(result)