def is_palindrome(word):
    word = word.lower()  
    reversed_word = word[::-1]
    
    return word == reversed_word

word = input()
if is_palindrome(word):
    print(f"palindrome")
else:
    print(f"not palindrome")