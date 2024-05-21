from caesar_shifts import shift_cipher
import string

def construct_cipher(keyword: str):
    keyword = list(keyword)
    cipher = keyword + [char for char in string.ascii_uppercase if char not in keyword]
    return cipher

def construct_table(keyword: str):
    cipher = construct_cipher(keyword)
    vigenere_table = []
    for i in range(26):
        vigenere_table.append(shift_cipher(-i, cipher))
    return vigenere_table