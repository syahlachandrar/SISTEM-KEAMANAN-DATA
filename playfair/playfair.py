def generate_playfair_matrix(key):
    # Inisialisasi matriks Playfair 5x5
    matrix = [['' for _ in range(5)] for _ in range(5)]
    
    # Inisialisasi set untuk memastikan karakter unik dalam kunci
    key_set = set()
    
    # Mengonversi kunci ke huruf besar dan menghilangkan karakter duplikat
    key = key.upper().replace("J", "I")
    for char in key:
        if char.isalpha() and char not in key_set:
            key_set.add(char)
    
    # Mengisi matriks dengan karakter-karakter kunci
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    k = 0
    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                key_set.add(key[k])
                k += 1
            else:
                while alphabet[0] in key_set:
                    alphabet = alphabet[1:]
                matrix[i][j] = alphabet[0]
                key_set.add(alphabet[0])
                alphabet = alphabet[1:]
    
    return matrix

def get_char_positions(matrix, char):
    # Mendapatkan posisi karakter dalam matriks
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key):
    # Membuat matriks Playfair
    matrix = generate_playfair_matrix(key)
    
    # Menyusun plaintext ke dalam pasangan huruf
    pairs = []
    i = 0
    while i < len(plaintext):
        pair = plaintext[i]
        if i + 1 < len(plaintext) and pair != plaintext[i + 1]:
            pair += plaintext[i + 1]
            i += 2
        else:
            pair += 'X'
            i += 1
        pairs.append(pair)

    # Proses enkripsi
    ciphertext = ''
    for pair in pairs:
        pos1 = get_char_positions(matrix, pair[0])
        pos2 = get_char_positions(matrix, pair[1])
        
        if pos1 is not None and pos2 is not None:
            row1, col1 = pos1
            row2, col2 = pos2

            if row1 == row2:
                # Jika huruf-huruf berada dalam baris yang sama
                ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Jika huruf-huruf berada dalam kolom yang sama
                ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                # Jika huruf-huruf membentuk persegi
                ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Contoh penggunaan
plaintext = "Syahla Chandra Ramadhania"
key = "Karanganyar"
plaintext = plaintext.upper().replace("J", "I").replace(" ", "")

ciphertext = playfair_encrypt(plaintext, key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
