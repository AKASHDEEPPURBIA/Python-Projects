import random
def dice_roll(amount: int = 2) -> list[int]:
    if amount<=0:
        raise ValueError

    rolls: list[int] = []
    global sum
    sum = 0
    for i in range(amount):
        random_roll: int = random.randint(1,6)
        sum+=random_roll
        rolls.append(random_roll)

    return  rolls

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            #printing the result of each dice rolled(1,6)
            print(*dice_roll((int)(user_input)), sep = ', ')
            #printing the sum of all the results of rolled dice
            print(sum)

        except ValueError:
            print('Please enter a valid number')

if __name__ == '__main__':
    main()




