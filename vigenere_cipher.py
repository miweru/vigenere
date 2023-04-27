import string
import unicodedata

def replace_umlauts(text):
    umlauts = {
        'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue',
        'ß': 'ss'
    }
    for key, value in umlauts.items():
        text = text.replace(key, value)
    return text

def replace_emoji(text):
    result = ''
    for char in text:
        try:
            char_name = unicodedata.name(char)
            if unicodedata.category(char) in ("So","Sk"):
                result += char_name.replace('_', ' ').lower() + ' '
            else:
                result += char
        except ValueError:
            result += char
    return result

def filter_supported_chars(text, alphabet):
    return ''.join([c for c in text if c in alphabet])

class VigenereCipher:
    def __init__(self, key):
        self.key = replace_umlauts(key.upper())
        self.alphabet = string.ascii_uppercase + ' .,!?;'

    def _shift_character(self, char, shift, operation):
        if char in self.alphabet:
            old_index = self.alphabet.index(char)
            if operation == "encrypt":
                new_index = (old_index + shift) % len(self.alphabet)
            elif operation == "decrypt":
                new_index = (old_index - shift) % len(self.alphabet)
            else:
                raise ValueError("Invalid operation")
            return self.alphabet[new_index]
        else:
            return char

    def _process_text(self, text, operation):
        text = replace_umlauts(text)
        text = replace_emoji(text)
        text = text.upper()
        text = filter_supported_chars(text, self.alphabet)
        processed_text = []
        key_index = 0

        for char in text:
            shift = self.alphabet.index(self.key[key_index])
            processed_char = self._shift_character(char, shift, operation)
            processed_text.append(processed_char)

            if char in self.alphabet:
                key_index = (key_index + 1) % len(self.key)

        return "".join(processed_text)

    def encrypt(self, plaintext):
        return self._process_text(plaintext, "encrypt")

    def decrypt(self, ciphertext):
        return self._process_text(ciphertext, "decrypt")
