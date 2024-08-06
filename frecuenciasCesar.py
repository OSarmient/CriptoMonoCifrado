from collections import Counter

# El texto cifrado
cipher_text = "JXYJJXUFWFQNJPUFNXFÑJQFXMJWQTXTDJPQFXYWNXYJIJPQZRITJXJPQNXQTUFNXFÑJIJPFUFLNRFFRYJWNTWVZJMJINGZÑFITZRFAJEQFXUFWFVZJPTAJFRGNJRKZJFVZNITRIJJPUWNRHNUNYTFUFWJHNTXTGWJPFYNJWWFIJXFUFWJHNJRITPZJLT"

# Contar la frecuencia de cada letra en el texto cifrado
frequency = Counter(cipher_text)

# Mostrar la frecuencia de cada letra
print("Frecuencia de letras en el texto cifrado:")
for letter, freq in frequency.most_common():
    print(f"{letter}: {freq}")

# Obtener la letra más frecuente
most_common_letter = frequency.most_common(1)[0][0]
print(f"Letra más frecuente: {most_common_letter}")

# Cifrado Cesar
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

# Alfabeto en español (incluye la Ñ)
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Desplazamiento para que la letra más frecuente se mapee a 'E' (letra más frecuente en español)
shift = alphabet.index(most_common_letter) - alphabet.index('E')

# Aplicar el cifrado de César con el desplazamiento calculado
plain_text = caesar_decrypt(cipher_text, shift, alphabet)

print("Texto descifrado (Cifrado de César):")
print(plain_text)
