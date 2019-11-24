secret_number = 1
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:

    guess = int(input('guess:'))
    guess_counter += 1
    if guess == secret_number:
        print('you won the game'+ " thanks for coming")
        break
else:
    print('you lose')

