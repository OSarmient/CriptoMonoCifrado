from collections import Counter

# El texto cifrado
cipher_text = "JXYJJXUFWFQNJPUFNXFÑJQFXMJWQTXTDJPQFXYWNXYJIJPQZRITJXJPQNXQTUFNXFÑJIJPFUFLNRFFRYJWNTWVZJMJINGZÑFITZRFAJEQFXUFWFVZJPTAJFRGNJRKZJFVZNITRIJJPUWNRHNUNYTFUFWJHNTXTGWJPFYNJWWFIJXFUFWJHNJRITPZJLT"

# Alfabeto en español (incluye la Ñ)
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Contar la frecuencia de cada letra en el texto cifrado
frequency = Counter(cipher_text)

# Frecuencia de letras en español (aproximado y ordenado por frecuencia)
spanish_frequency = "EAOSRNIDLCUTPMBFGVQGHJÑKXZYW"

# Crear un diccionario de mapeo de letras basado en la frecuencia
mapping = {}
for (cipher_letter, _), plain_letter in zip(frequency.most_common(), spanish_frequency):
    mapping[cipher_letter] = plain_letter

print(mapping)

# Mostrar el mapeo inicial
print("Mapeo inicial:")
for cipher_letter, plain_letter in mapping.items():
    print(f"{cipher_letter} -> {plain_letter}")

# Descifrar el texto usando el mapeo de frecuencias
plain_text = ''.join(mapping.get(char, char) for char in cipher_text)

print("Texto descifrado (aproximado):")
print(plain_text)

# Mapeo ajustado manualmente (si es necesario)
# Ajustes basados en observaciones del texto descifrado inicial
adjusted_mapping = {
    'J': 'E', 'X': 'L', 'Y': 'I', 'U': 'R', 'F': 'A', 'W': 'N', 'Q': 'D', 'N': 'O',
    'P': 'T', 'I': 'S', 'R': 'C', 'Z': 'U', 'Ñ': 'M', 'V': 'P', 'G': 'V', 'H': 'Q',
    'M': 'Y', 'L': 'B', 'A': 'H', 'D': 'G', 'E': 'J', 'K': 'Ñ', 'T': 'K'
}

# Ajustes adicionales basados en patrones observados
# Ajustamos algunas letras para tratar de encontrar palabras más legibles
adjusted_mapping['J'] = 'E'  # Cambiamos J -> E
adjusted_mapping['X'] = 'L'  # Cambiamos X -> L
adjusted_mapping['Y'] = 'I'  # Cambiamos Y -> I
adjusted_mapping['U'] = 'R'  # Cambiamos U -> R
adjusted_mapping['F'] = 'A'  # Cambiamos F -> A
adjusted_mapping['W'] = 'N'  # Cambiamos W -> N
adjusted_mapping['Q'] = 'D'  # Cambiamos Q -> D
adjusted_mapping['N'] = 'O'  # Cambiamos N -> O
adjusted_mapping['P'] = 'T'  # Cambiamos P -> T
adjusted_mapping['I'] = 'S'  # Cambiamos I -> S
adjusted_mapping['R'] = 'C'  # Cambiamos R -> C
adjusted_mapping['Z'] = 'U'  # Cambiamos Z -> U
adjusted_mapping['Ñ'] = 'M'  # Cambiamos Ñ -> M
adjusted_mapping['V'] = 'P'  # Cambiamos V -> P
adjusted_mapping['G'] = 'V'  # Cambiamos G -> V
adjusted_mapping['H'] = 'Q'  # Cambiamos H -> Q
adjusted_mapping['M'] = 'Y'  # Cambiamos M -> Y
adjusted_mapping['L'] = 'B'  # Cambiamos L -> B
adjusted_mapping['A'] = 'H'  # Cambiamos A -> H
adjusted_mapping['D'] = 'G'  # Cambiamos D -> G
adjusted_mapping['E'] = 'J'  # Cambiamos E -> J
adjusted_mapping['K'] = 'Ñ'  # Cambiamos K -> Ñ
adjusted_mapping['T'] = 'K'  # Cambiamos T -> K

# Descifrar el texto usando el mapeo ajustado
adjusted_plain_text = ''.join(adjusted_mapping.get(char, char) for char in cipher_text)

print("Texto descifrado (ajustado):")
print(adjusted_plain_text)
