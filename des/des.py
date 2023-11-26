from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

plain_text = "teknikinformatika"

# 8 byte block 
key = b'inikunci' 

# Menetapkan panjang data yang akan dienkripsi
BLOCK_SIZE = 8

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(plain_text.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

print ("Plain Teks : ", plain_text)

print("Hasil Enkripsi : ", encrypted_text)

key = b'inikunci' # 8 byte block
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print("Hasil Dekripsi : ", decrypted_text.decode())