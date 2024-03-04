age=int(input())
ages=list()
while age != -1:
    if (age >= 10) and (age <= 90):
        ages.append(age)

    age=int(input())
 
MaxAge=max(ages)
print(MaxAge)
   