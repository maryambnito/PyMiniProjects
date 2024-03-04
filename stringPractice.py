# def delete_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     silent_letters = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
#     modified_string = ""
    
#     for char in input_string:
#         if char in silent_letters:
#             modified_string += '.' + char.lower()
    
#     return modified_string

# input_string = input()
# result = delete_vowels(input_string)
# print(result)
def delete_vowels(str):
    vowels="a,e,i,o,u,A,E,I,O,U"
    vowel_list=vowels.split(',')
    modified_str=""
    print (vowel_list)
    for char in str:
        if char not in vowel_list:
            modified_str+= "." + char.lower()
    return modified_str
str=input()
result=delete_vowels(str)
print(result)        
