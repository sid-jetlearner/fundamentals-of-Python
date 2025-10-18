import random
num=random.randint(80,100)
for i in range(5):
    guess=int(input('enter a number between 80 and 100'))
    if num==guess:
        print('Correct')
        break 
    elif num>guess:
        print('Guess a higher number')
    elif num<guess:
        print('Guess a lower number')
