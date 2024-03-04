age=int(input())
ages=list()
while age != -1:
    if (age >= 10) and (age <= 90):
        ages.append(age)

    age=int(input())
 
MaxAge=max(ages)
indexMaxAge=ages.index(MaxAge)
ages.pop(indexMaxAge)
MaxAge2=max(ages)
print(MaxAge,"",MaxAge2)



   