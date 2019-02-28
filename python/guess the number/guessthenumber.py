import random
number = int(random.randint(0, 20))
while True:
    print('guess the number, type giveup to quit!')
    guess = input('>')
    if guess == int(number):
        print('you guessed right!')
        break
    elif guess == 'giveup':
        print('the number was: {}'.format(number))
        break
    else:
        print('WRONG!')