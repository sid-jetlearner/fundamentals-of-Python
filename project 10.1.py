import random
numbers=[1,2,3,4,5,6,7,8,9,0]
alphabets="abcdefghijklmnopqrstuvwxyz"
symbols="!@£$%^&*()_+-="
a=random.choice(alphabets)
b=random.choice(alphabets)
c=random.choice(alphabets)
d=random.choice(alphabets)
e=random.choice(alphabets)
f=random.choice(symbols)
g=random.choice(symbols)
h=random.choice(numbers)
print(a+f+c+e+d+str(h)+g)
feedback=input("Do you like the password? If not, enter your feedback here...")