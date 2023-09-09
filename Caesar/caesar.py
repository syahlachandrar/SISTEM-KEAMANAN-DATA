#!/usr/bin/env python
# coding: utf-8

# In[9]:


import string

#inputan plaintext yang akan dienkripsi
plaintext = input("Masukkan teks yang akan dienkripsi: ")

def caesar_encrypt(plaintext): #fungsi
    res = "" #inisialisasi var
    for x in range(len(plaintext)):
        if plaintext[x].isupper(): #jika karakter kapital
            enc = (string.ascii_uppercase.index(plaintext[x]) + 42) % 26
            res += string.ascii_uppercase[enc]
        elif plaintext[x].islower(): #jika karakter huruf kecil
            enc = (string.ascii_lowercase.index(plaintext[x]) + 42) % 26
            res += string.ascii_lowercase[enc]
        elif plaintext[x].isdigit(): #jika karakter angka
            res += chr(((ord(plaintext[x]) - ord('0') + 42) % 10) + ord('0'))
        else:
            #jika karakter bukan huruf tidak berubah
            res += plaintext[x]
    return res

#pemanggilan fungsi
encrypted_text = caesar_encrypt(plaintext)
print("Teks terenkripsi:", encrypted_text)


# In[10]:


import string

# Inputan ciphertext yang akan didekripsi
ciphertext = input("Masukkan teks yang akan didekripsi: ")

def caesar_decrypt(ciphertext): #fungsi untuk decrypt
    res = "" #inisialisasi variabel
    for x in range(len(ciphertext)):
        if ciphertext[x].isupper(): #jika karakter kapital
            dec = (string.ascii_uppercase.index(ciphertext[x]) - 42) % 26
            res += string.ascii_uppercase[dec]
        elif ciphertext[x].islower(): #jika karakter kecil
            dec = (string.ascii_lowercase.index(ciphertext[x]) - 42) % 26
            res += string.ascii_lowercase[dec]
        elif ciphertext[x].isdigit(): #jika karakter angka
            res += chr(((ord(ciphertext[x]) - ord('0') - 42) % 10) + ord('0'))
        else:
            #karakter bukan huruf atau angka maka tidak berubah
            res += ciphertext[x]
    return res

#pemanggilan fungsi
decrypted_text = caesar_decrypt(ciphertext)
print("Teks terdekripsi:", decrypted_text)


# In[ ]:





# In[ ]:




