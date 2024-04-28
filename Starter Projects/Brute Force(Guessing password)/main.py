import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common math : {match} (#{i})'

# This code essentially iterates through all possible combinations of characters
# of a specified length and checks each combination against a target word or password
# until a match is found. It then returns a message indicating how many attempts
# it took to crack the word.

def brute_force(word: str, length: int, digits: bool, symbols: bool) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat = length):

        attempts+=1
        guess: str = ''.join(guess)

        if guess == word:
            return f'{word} was crackeds in {attempts} guesses'
        print(guess, attempts)

def main():
    print('Searching...')
    password: str = 'gh@1'

    #get the start_time
    start_time = time.perf_counter()

    #search for common word before actually using brute force
    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, 4, True, True):
            print(cracked)
        else:
            print('There is no match')

    #get the end_time
    end_time = time.perf_counter()

    #show the time taken in seconds
    print((round(end_time-start_time)), 's')

if __name__ == '__main__':
    main()

