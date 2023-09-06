# Tuplas

# ele é imutavel

frutas = ("laranja", "pera", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

print(frutas[2])

# matriz

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

# iterar

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#de funções, tem a count, index e len, funcionam igual nas listas