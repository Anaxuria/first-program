# Listas em Python

frutas = ["laranja", "Maça", "Uva", "Pera"]
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

# Acesso Direto

print(frutas[1])
print(frutas[-1])

# Matriz

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[2][-1])

# Fatiamento 

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[::])
print(lista[::-1])

# Iterar listas e funçaõ enumerate

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# filtro

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
#pares = [numero for numero in numeros if numero % 2 == 0]

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"\nPares: {pares}")
# Modificando valores

nums = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
#quadrado = [num ** 2 for num in nums]

for num in nums:
    quadrado.append(num **2)

print(f"\nAo quadrado: {quadrado}")
## Metodos da classe list

lista = []

lista.append(1) #add itens
lista.append("Python")
lista.append([40, 30, 20])

print("\n",lista)

lista.clear() #limpa a lista

print(lista)

lista.append(1) #add itens
lista.append("Python")
lista.append([40, 30, 20])

lista2 = lista.copy() #faz uma copia da lista

print(lista)
print(lista2)
print("Id lista 1: ",id(lista), "\nId lista 2: ",id(lista2),"\n")

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho")) #contar quandos daquele item tem
print(cores.count("azul"))
print(cores.count("verde"),"\n")

linguagens = ["python", "js", "c"]

print(linguagens) #juntar 2 listas

linguagens.extend(["java", "c++"])

print(linguagens)

print(linguagens.index("java")) #mostra qual a posição. obs: se tiver revetido, mostra a posição do primeiro.
print(linguagens.index("python"))

print(linguagens.pop()) #remove elementos em estrutura pilha (ex: pilha de pratos)
print(linguagens.pop())
print(linguagens.pop(0))

print(linguagens)

linguagens.remove("js") #remove o item diretamente

print(linguagens)

cantores = ["taylor swift", "lady gaga", "maroon5", "britney spears"]

cantores.reverse() #inverte a ordem da lista

print(cantores)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  #ordem alfabetica
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #inverte a ordem alfabetica
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  #menor numero de caracteres
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #maior numero de caracteres
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  #mostra o tamanho do elemento

print(sorted(linguagens, key=lambda x: len(x)))  #uma função que deixa ele em ordem do menor pro maior
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) #uma função que deixa ele e, ordem do maior pro menor
print(sorted(linguagens)) #função que deixa em ordem alfabetica