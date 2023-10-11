def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text



def decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key_shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - key_shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Proses Login
def main():
    username = "imam"
    password = "solehudin"
    key = "kuncisaya"  # kunci rahasia

    # Enkripsi password sebelum disimpan
    encrypted_password = encrypt(password, key)

    # Simpan username dan password terenkripsi dalam database
    database = {"username": username, "password": encrypted_password}

    # Login
    input_username = input("Masukkan Username anda: ")
    input_password = input("Masukkan Password anda: ")

    if input_username == database["username"] and decrypt(database["password"], key) == input_password:
        print("Proses Login anda berhasil!")

        # Tampilkan hasil enkripsi dan dekripsi
        print(f"Password terenkripsi: {encrypted_password}")
        decrypted_password = decrypt(database["password"], key)
        print(f"Password terdekripsi: {decrypted_password}")
    else:
        print("Proses Login anda gagal!")

if __name__ == "__main__":
    main()
