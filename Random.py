import random
target_number = random.randint(1, 100)
for attempt in range(10):
    guess = int(input(f'Guess a number between 1 and 100: '))
    if guess < target_number:
        print(f'Sorry {guess} is too low!')
    elif guess > target_number:
        print(f'Sorry {guess} is too high!')
    else:
        print(f'You guessed {guess}')
        break