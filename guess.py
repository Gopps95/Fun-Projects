import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess the number b/w 1 and {x}:"))
        if guess < random_number:
            print('Sorry too low')
        elif guess > random_number:
            print("Too high")

    print(f'Yay Congrats {random_number} is correct')

    
guess(10)