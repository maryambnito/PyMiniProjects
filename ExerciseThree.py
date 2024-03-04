num=int(input())
reverse=0
if (num>=100) and (num<1000):
    while num>0 :
        reminder=num%10
        reverse=(reverse*10)+reminder
        num=num//10

    print(reverse*2)
    