print("Hello World!")

idade = input("Digite sua idade: ")

idade = int(idade)

if idade < 0:
    print("Você nem nasceu")
elif idade < 18:
    print("Você é menor de idade")
elif idade < 60:
    print("Você é maior de idade")
else: 
    print("Você é idoso")

print(f"Você tem {idade} anos")

nota = input("Digite sua nota: ")

status = "Aprovado" if int(nota) >= 6 else "Reprovado"

print(status)