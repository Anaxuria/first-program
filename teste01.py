saldo_atual = float(input("Digite o seu saldo atual: "))
valor_deposito = float(input("Digite o valor que você deseja depositar: "))
valor_retirada = float(input("Digite o valor que você deseja retirar: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = (saldo_atual + valor_deposito) - valor_retirada
#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print("Saldo atualizado na conta: ", saldo_atual)