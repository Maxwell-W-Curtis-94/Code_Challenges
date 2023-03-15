def digit_of_life(number):
    digits = [int(x) for x in str(number)]
    number = sum(digits)
    if number < 10:
        return number
    return digit_of_life(number)


print(digit_of_life(19940623))
