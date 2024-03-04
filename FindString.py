def find_chars(word):
    if "AB" in word and "BA" in word:
        ab_index = word.find("AB")
        ba_index = word.find("BA")
        if (abs(ab_index - ba_index) > 1) or (abs(ab_index - ba_index) == 1 and "AB" in word[ba_index + 2:]) or (abs(ab_index - ba_index) == 1 and "BA" in word[ab_index + 2:]):
            return "YES"
    
    return "NO"   
   

word = input()
result = find_chars(word)
print(result)