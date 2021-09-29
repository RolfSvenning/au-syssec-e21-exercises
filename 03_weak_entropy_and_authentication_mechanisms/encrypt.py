#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES


def encrypt(input_file, output_file):
    random.seed(int(time.time()))
    key = random.randbytes(16)
    aes = AES.new(key, AES.MODE_GCM)

    with open(input_file, 'rb') as f_in:
        data = f_in.read()
    ciphertext, tag = aes.encrypt_and_digest(data)

    with open(output_file, 'wb') as f_out:
        f_out.write(aes.nonce)  # 16 bytes
        f_out.write(tag)        # 16 bytes
        f_out.write(ciphertext) # len(data) bytes


def decrypt(input_file, output_file):
    print("here")
    nonce = "28 E3 E4 CB  40 D3 A5 71  0D 66 05 58  35 89 59 83"
    tag = "4C 69 33 EB  6B 86 70 D6  31 8E 34 B1  AF D9 0A D7"

    for i in range(int(time.time()) - 100, int(time.time())):
        random.seed(i)
        key = random.randbytes(16)
        aes = AES.new(key, AES.MODE_GCM)

        with open(input_file, 'rb') as f_in:
            data = f_in.read()
        ciphertext, tag = aes.decrypt_and_verify(data, )

        with open(output_file, 'wb') as f_out:
            f_out.write(aes.nonce)  # 16 bytes
            f_out.write(tag)        # 16 bytes
            f_out.write(ciphertext) # len(data) bytes
    return 0



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <src-file> <dst-file>', file=sys.stderr)
        exit(1)
    decrypt(sys.argv[1], sys.argv[2])
