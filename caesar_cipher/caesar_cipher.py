import string
import caesar_shifts

def format_message(message: str):
    formatted_message = []
    message = message.upper()
    for char in message:
        if char in string.ascii_uppercase:
            formatted_message.append(char)
    formatted_message = "".join(formatted_message)
    return formatted_message

def caesar_cipher(message: str, shift_num: int):
    cipher = caesar_shifts.shift_cipher(shift_num, list(string.ascii_uppercase))

    encoded_message = []
    for char in format_message(message):
        encoded_message.append(cipher[list(string.ascii_uppercase).index(char)])
    encoded_message = "".join(encoded_message)
    return encoded_message