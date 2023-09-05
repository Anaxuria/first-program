# python com strings

curso = "pYtHoN"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso = "   Python "

print(curso.strip()+ ".")
print(curso.lstrip()+ ".")
print(curso.rstrip()+ ".")

curso = "Python"

print(curso.center(10,'#'))
print(".".join(curso))

word = input("\n\nDigite uma palavra: ")

print("\n",word.upper())
print(word.lower())
print(word.title())

print(word.strip()+ ".")
print(word.lstrip()+ ".")
print(word.rstrip() + ".")

print(word.center(10,'#'))
print(".".join(word))

# interpolação de variaveis

nome = "ana"
idade = 18

print("Nome: %s \nIdade: %i" % (nome, idade))
print("Nome: {} \nIdade: {}".format(nome, idade))
print("Nome: {1} \nIdade: {0}".format(idade, nome))
print("Nome: {name} \nIdade: {age}".format(name=nome, age=idade))
print(f"Nome: {nome} \nIdade: {idade}")

# Fatiamento de string

nome = "Ana Julia Garcia"

print("\n",nome[0])
print(nome[:4])
print(nome[10:])
print(nome[4:9])
print(nome[:])
print(nome[::-1])

# string de varias linhas

print(f"""\nOlá meu nome é {nome},
Tenho {idade}, gosto de filmes,
flw, at[+é a proxima!!""")