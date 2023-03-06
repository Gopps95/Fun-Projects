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



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback !='c' and low!=high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high, too low, or correct')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess + 1

    print("Its correct")
computer_guess(10)
guess(10)
