scores=[5]
def numbers():
    num=1
    while num <= 30: 
        number=abs(int(input()))
        if (number == 1) or (number == 0) or (number == 3):
            scores.append(number)
            num+=1    

        
numbers() 
win=scores.count(3) 
scores.remove(5)  
equal=scores.count(1)
count=(win * 3) + equal 
print(count," ",win)    

