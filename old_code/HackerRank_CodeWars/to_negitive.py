def make_negative(number):
    return -abs(number)


if __name__ == '__main__':
    for num in [1, 0, -1]:
        print(make_negative(number=num))
