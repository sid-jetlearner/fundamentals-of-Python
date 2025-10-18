m1=int(input('Enter your Maths marks here:'))
m2=int(input('Enter your English marks here:'))
m3=int(input('Enter your Science marks here:'))
m4=int(input('Enter your Geography marks here:'))
m5=int(input('Enter your History marks here:'))
sum=m1+m2+m3+m4+m5
average=sum/5
if average>90:
    print('Your grade is A')
elif average>80 and average<91: 
    print('Your grade is B')
elif average<81 and average>60:
    print('Your grade is C')
elif average<61 and average>40:
    print('your grade is D')
elif average<41 and average>20:
    print('Your grade is E')
elif average<21 and average>0:
    print('Your grade is F')