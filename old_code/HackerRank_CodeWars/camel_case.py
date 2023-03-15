import re


def to_underscore(string):
    if string is not str:
        string = str(string)
    split = re.sub(r"(\w)([A-Z])", r"\1 \2", string).split(" ")
    new_string = ""
    for tok in split:
        new_string += tok.lower() + "_"
    return new_string[:-1]


def camel_case(string):
    value = ''
    for line in string.split(' '):
        value += line.strip().capitalize()
    return value
