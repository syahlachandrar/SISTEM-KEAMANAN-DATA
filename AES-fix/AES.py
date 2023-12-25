from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Generate a salt
salt = get_random_bytes(16)

# Generate a derived key from a passphrase
passphrase = "Belajar AES easy"
key = PBKDF2(passphrase, salt, dkLen=32, count=1000000)  # Ganti dkLen sesuai dengan panjang yang Anda inginkan

# Create a new instance of the cipher
cipher = AES.new(key, AES.MODE_EAX)

# Data to be encrypted
data = "semangat ya guys".encode()

# Nonce is a random value generated each time we instantiate the cipher using new()
nonce = cipher.nonce

# Encrypt the data
ciphertext = cipher.encrypt(data)

# Print the encrypted data
print("Cipher text:", ciphertext)

# Generate a new instance with the key and nonce same as the encryption cipher
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Decrypt the data
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext.decode())