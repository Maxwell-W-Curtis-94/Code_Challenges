def my_split(string):
    split_string = []
    hold = ''
    for char in string:
        if ' ' not in char:
            hold += char
        else:
            if hold:
                split_string.append(hold)
            hold = ''
    else:
        if hold:
            split_string.append(hold)
    return split_string


print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
