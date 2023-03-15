def generate_hashtag(s):
    if s == "":
        return False
    s = s.split(" ")
    words = ""
    for i in s:
        words += i.capitalize()
    if len(words) > 140:
        return False
    else:
        return "#" + words


def generate_hashtag_2(s):
    s = s.split(" ")
    htag = "#"
    for tok in s:
        htag += tok.capitalize()
    if len(htag) > 140 or htag == "#":
        return False
    else:
        return htag
