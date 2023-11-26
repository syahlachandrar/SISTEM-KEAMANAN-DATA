#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def text_to_matrix(text, n):
    #fungsi untuk mengubah teks menjadi matriks
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('a'))
    
    #Mengisi matriks dengan 0 jika panjang teks bukan kelipatan n
    while len(matrix) % n != 0:
        matrix.append(1)
    
    #Membagi matriks menjadi matriks n x n
    matrix = np.array(matrix).reshape(-1, n)
    
    return matrix

def matrix_to_text(matrix):
    #mengubah matriks menjadi teks
    text = ""
    for row in matrix:
        for val in row:
            text += chr(val + ord('a'))
    
    return text

def encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    plain_matrix = text_to_matrix(plain_text, n)
    
    #perkalian matriks dan modulus dari hasil perkalian
    cipher_matrix = np.dot(plain_matrix, key_matrix) % 26
    
    #konversi matriks hasil modulus menjadi teks
    cipher_text = matrix_to_text(cipher_matrix)
    
    return cipher_text


plain_text = input("masukkan plain text: ")
key_matrix = np.array([[18, 7, 13], [24, 11, 3], [0, 2, 17]])
encrypted_text = encrypt(plain_text, key_matrix)
print("Kunci Matriks:")
print(key_matrix)
print("Teks Enkripsi:", encrypted_text)


# In[ ]:





# In[ ]:




