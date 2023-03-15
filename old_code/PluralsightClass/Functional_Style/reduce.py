from functools import reduce
import operator

"""
Repeatedly applies a two-argument function to an accumulated values and the next element from a sequence

the initial value can be the first element in the input sequence or an optional argument

the final accumulated - or reduced - value is returned

does whatever you tell it to do to a list tell you only have one left
"""

print(reduce(operator.add, [1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)

print(accumulator)


def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x * y


print(reduce(mul, range(1, 10)))
