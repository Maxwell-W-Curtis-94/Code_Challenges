import string

alphabet = list(string.ascii_lowercase)


def caesar_cipher(_shift, text):
    encoded_text = ''
    for letter in text:
        if letter not in alphabet:
            encoded_text += letter
        else:
            index = alphabet.index(letter)
            new_index = index + _shift
            if new_index > 26:
                new_index -= 26
            encoded_text += alphabet[new_index]

    return encoded_text


shift = 10
print(caesar_cipher(shift, f'the text is shifted by {shift}'))
