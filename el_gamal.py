import random

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def elgamal_encrypt(plaintext_number, p, e1, e2):
    r = random.randint(1, p - 1)
    c1 = modular_exponentiation(e1, r, p)
    c2 = (plaintext_number * modular_exponentiation(e2, r, p)) % p
    return c1, c2

def elgamal_decrypt(c1, c2, d, p):
    s = modular_exponentiation(c1, d, p)
    s_inv = mod_inverse(s, p)
    plaintext_number = (c2 * s_inv) % p
    return plaintext_number

if __name__ == "__main__":
    p = int(input("Enter a large prime number (p): "))
    e1 = int(input("Enter the base (e1): "))
    d = int(input("Enter the private key (d): "))

    e2 = modular_exponentiation(e1, d, p)

    plaintext_number = int(input("Enter the numeric plaintext to encrypt: "))

    c1, c2 = elgamal_encrypt(plaintext_number, p, e1, e2)
    print(f"Ciphertext: (c1={c1}, c2={c2})")

    decrypted_number = elgamal_decrypt(c1, c2, d, p)
    print(f"Decrypted: {decrypted_number}")
