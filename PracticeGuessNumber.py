import random
num1=1
num2=99
guess=random.randint(num1,num2)
print(guess)
correctNumber=input()
while correctNumber != 'd':
   
    if correctNumber == 'b':
        num1= guess+1 
        guess=random.randint(num1,num2)   
        print(guess)
        correctNumber=input()
    elif correctNumber == 'k':
        num2=guess-1    
        guess=random.randint(num1,num2)   
        print(guess)
        correctNumber=input()

print('you won !!')
