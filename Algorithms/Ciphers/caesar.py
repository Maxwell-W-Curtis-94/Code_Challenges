import string

alphabet = list(string.ascii_lowercase)


def caesar_cipher1(shift, text):
    encoded_text = ''
    for letter in text:
        if letter not in alphabet:
            encoded_text += letter
        else:
            index = alphabet.index(letter)
            new_index = index + shift
            if new_index > 26:
                new_index -= 26
            encoded_text += alphabet[new_index]

    return encoded_text


print(caesar_cipher1(10, 'the text is shifted by one'))
