import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print(f"Well, {myName}, I am thinking of a number between 1 and 20.")
print()

for guessesTaken in range(6):
    guessesRemaining = 6 - guessesTaken
    print(f'Take a guess. You have {guessesRemaining} guesses left')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low')
        print()
    
    if guess > number:
        print('Your guess is too high')
        print()
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print()
    print(f'Good job, {myName}! You guessed my number in {guessesTaken} guesses!')

if guess != number:
    number = str(number)
    print()
    print(f'Nope. The number I was thikning of  was {number}.')


# from Invent Your Own Computer Games with Python