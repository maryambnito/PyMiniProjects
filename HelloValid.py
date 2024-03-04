def say_hello(word):
    hello = "hello"
    i = 0
    for char in word:
        if char == hello[i]:
            i += 1
            if i == len(hello):
                return True
    return False

word = input()

if say_hello(word):
    print("YES")
else:
    print("NO")

