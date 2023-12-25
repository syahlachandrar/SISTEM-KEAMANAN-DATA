def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                ciphertext += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, a, b):
    mod_inverse = pow(a, -1, 26)  # Calculating the modular multiplicative inverse
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((mod_inverse * (ord(char) - ord('A' )) - b) % 26 + ord('A'))
            else:
                plaintext += chr((mod_inverse * (ord(char) - ord('a')) - b) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "syahlachandrarmdn"
a = 5
b = 7

# Enkripsi
encrypted_text = encrypt(plaintext, a, b)
print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)

# Dekripsi
decrypted_text = decrypt(encrypted_text, a, b)
print("Decrypted:", decrypted_text)
