def caesar_decrypt(cipher_text, shift, alphabet):
    decrypted_text = []
    for char in cipher_text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx - shift) % len(alphabet)
            decrypted_text.append(alphabet[new_idx])
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# El texto cifrado
cipher_text = "JXYJJXUFWFQNJPUFNXFÑJQFXMJWQTXTDJPQFXYWNXYJIJPQZRITJXJPQNXQTUFNXFÑJIJPFUFLNRFFRYJWNTWVZJMJINGZÑFITZRFAJEQFXUFWFVZJPTAJFRGNJRKZJFVZNITRIJJPUWNRHNUNYTFUFWJHNTXTGWJPFYNJWWFIJXFUFWJHNJRITPZJLT"

# Alfabeto en español (incluye la Ñ)
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Probar todos los posibles desplazamientos
for shift in range(len(alphabet)):
    decrypted_text = caesar_decrypt(cipher_text, shift, alphabet)
    print(f"Desplazamiento {shift}:")
    print(decrypted_text)
    print("\n")
