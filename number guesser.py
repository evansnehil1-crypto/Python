print("=======================================")
print("    Welcome To Number Guessing Game!   ")
print("=======================================")

secret = 27
attempts = 0
max_attempts = 5
won = False

while attempts < max_attempts and won == False:

    guess = int(input("Guess the number (1-50): "))
    attempts = attempts + 1

    if guess == secret:
        print("\n Cronratulations you guessed the secret number!")
        won = True

    else:

        if guess > secret:
            difference = guess - secret
        else:
            difference = secret - guess

        if difference >= 40:
            print("🧊 ice cold")
        elif difference >= 30:
            print("🌡️ warm")
        elif difference >= 20:
            print("🔥 hot")
        elif difference <= 10:
            print("🥶 cold")

else:
    attempts == 5
    print("\n you have lost")
     