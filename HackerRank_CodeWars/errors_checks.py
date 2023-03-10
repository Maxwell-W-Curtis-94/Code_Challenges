"""
playing with assert validation
"""


def read_int(prompt, _min, _max):
    valid = False
    while not valid:
        try:
            number = int(input(prompt))
            assert number <= _max
            assert number >= _min
            valid = True
            return number
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print(f"Error: the value is not within permitted range ({_min}..{_max})")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
