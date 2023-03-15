def rgb(r, g, b):
    def limit(num):
        if num < 0:
            return 0
        if num > 255:
            return 255
        return num

    result = ''
    for i in r, g, b:
        i = limit(i)
        i = str(hex(i)).replace("0x", '').upper()
        if len(i) < 2:
            i = i.zfill(2)
        result += i
    return result


def better_rgb(r, g, b):
    def limit(num):
        if num < 0:
            return 0
        if num > 255:
            return 255
        return num

    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))


if __name__ == '__main__':
    print(rgb(255, 255, 255))  # returns FFFFFF
    print(rgb(255, 255, 300))  # returns FFFFFF
    print(rgb(0, 0, 0))  # returns 000000
    print(rgb(148, 0, 211))  # returns 9400D3
