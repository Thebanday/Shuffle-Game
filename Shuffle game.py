from random import shuffle


def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)

    return mylist


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

mylist = [' ','O',' ']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)
