def is_isogram(string):
    # string = string.lower()
    # for i in string:
    #     if len(set(string)) < len(string):
    #         return False
    #     elif i.isdigit():
    #         return False
    # return True
    return len(string) == len(set(string.lower()))


print(is_isogram(''))
print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("mo0se"))
