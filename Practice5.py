def count_divisors(num): 
    count = 0 
    for i in range(1, num+1): 
        if num % i == 0:
            count += 1 
    return count

numbers = []
for _ in range(1,21):
    num = int(input())
    numbers.append(num)
numbers.sort()
max_divisors = 0
number_with_max_divisors = 0

for num in numbers:
    divisors = count_divisors(num)
    if divisors > max_divisors:
        max_divisors = divisors
        number_with_max_divisors = num
    elif divisors == max_divisors and num > number_with_max_divisors:
        number_with_max_divisors = num

print(number_with_max_divisors,"",max_divisors)
