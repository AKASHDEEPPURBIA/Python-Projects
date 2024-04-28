from random import choice

def run_game():
    word: str = choice(['Akash', 'Ghoda', 'Purbia'])

    username: str = input(f'Enter your name ')
    print(f'Hi {username}, Welcome to the Hangerman')

    guessed: str = ''
    tries: int = 3 # Number of tries we have

    while tries>0:
        blanks: int = 0

        print('Word: ', end='') # no new line

        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1

        print() #add a blank line

        if blanks==0:
            print('You got it!')
            break

        guess: str = input('Guess the char: ')
        if (len(guess)>1):
            print(f'Please choose only 1 letter at a time')
            continue
        if guess in guessed:
            print(f'You have already used this char, please try a different one!')
            continue

        guessed+=guess

        if guess not in word:
            tries-=1
            print(f'you have guessed the incorrect letter, {tries} tries are remaining')

            if tries==0:
                print(f'No more tries remaining. You Lose!')
                break

if __name__ == '__main__':
    run_game()
