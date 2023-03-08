# RC4 en python
# Cruz Rangel Leonardo Said
# Criptografia

# Leemos de stdin y colocamos cada linea en un arreglo
import fileinput

lines = []
for line in fileinput.input():
    lines.append(line.strip()) #elimina los saltos de linea

#KSA
def KSA(k): # Input: key K of l bytes
    # Inicialización de la matriz 's' en la permutación identidad
    s = list(range(256))
    # Valor inicial del índice 'j'
    j = 0
    # Procesamiento de 's' durante 256 iteraciones y mezcla de bytes
    for i in range (0, 256):
        j = (j + s[i] + k[i % len(k)]) % 256
        s[i], s[j] = s[j], s[i] #swap
    return s # Output: estado interno st0

#PRGA
def PRGA(s):
    # Valor inicial de los índices
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i] # swap
        K = s[(s[i] + s[j]) % 256]
        yield K # devuelve el valor de K y pausa temporalmente su ejecución

# RC4
def RC4_algorithm (key, plaintext):
    # Inicializamos el estado interno de 's'
    s = KSA(key)
    # Genera la secuencia pseudoaleatoria
    keystream = PRGA(s)
    # Ciframos el mensaje combinando cada byte del mensaje con el siguiente byte en la secuencia pseudoaleatoria
    ciphertext = bytes([p ^ next(keystream) for p in plaintext])
    return ciphertext.hex().upper()

clave = lines[0].encode('utf-8')

textoplano = lines[1].encode('utf-8')

print(RC4_algorithm(clave, textoplano))