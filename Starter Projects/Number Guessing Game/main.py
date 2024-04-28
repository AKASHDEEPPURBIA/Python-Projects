from random import randint

lower_number, higher_number = 1, 10

random_number: int =  randint(lower_number, higher_number)

print(f'guess the number in the range from {lower_number} to {higher_number}')

n = 3;
i=0;

#you can only guess three times
while i<n:
    try:
        user_guess: int = int(input('guess: '))
    except ValueError as e:
        print(f'Please enter a valid number')
        continue

    if user_guess > random_number:
        print(f'please guess a lower number')
    elif user_guess < random_number:
        print(f'please guess a higher number')
    else:
        print(f'you guessed it!')
        break
    i+=1


