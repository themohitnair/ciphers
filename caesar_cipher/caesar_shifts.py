def cipher_shift_right(cipher: list):
    return [cipher[-1]] + cipher[:-1]

def cipher_shift_left(cipher: list):
    return cipher[1:] + [cipher[0]]

def shift_cipher(shift_num: int, cipher: list):
    if shift_num < 0:
        for _ in range(-1 * shift_num):
            cipher = cipher_shift_left(cipher)

    else:
        for _ in range(shift_num):
            cipher = cipher_shift_right(cipher)

    return cipher

