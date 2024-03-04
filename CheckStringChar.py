def check_word(word):
    upper_count=0
    lower_count=0
    count=0
    for i in word:
        if i == (word[count].upper()):
            upper_count += 1
            count+=1
        else:
            lower_count += 1    
            count+=1

    if upper_count > lower_count:
        return word.upper()
    else:
        return word.lower()
    
word = input()
result = check_word(word)
print(result)


