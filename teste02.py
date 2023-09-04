idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Você nem nasceu!")
elif idade < 16:
    print("Você não pode votar!")
elif idade < 18 or idade > 70:
    print("Você não é obrigado a votar!")
    op = int(input("Você vai votar? \n1- Vou; \n2- Não vou. \n"))

    match op:
        case 1:
            voto = int(input("Digite numero de voto: \n12- Ciro; \n13- Lula; \n22- Bolsonaro; \n00- Nulo. \n"))

            match voto:
                case 12:
                    print("Você votou no Ciro Gomes!")
                case 13:
                    print("Você votou no Lula!")
                case 22:
                    print("Você votou no Bolsonaro!")
                case 00: 
                    print("Você votou nulo!")
                case _:
                    print("O numero digitado não é valido, foi anulado!")
        
        case 2:
            print("Esta tudo certo, muito obrigado!")

        case _:
            print("Valor não valido, neste caso, você não votará este ano.")

else:
    print("Você é obrigado a votar!")

    voto = int(input("Digite numero de voto: \n12- Ciro; \n13- Lula; \n22- Bolsonaro; \n00- Nulo. \n"))

    match voto:
        case 12:
            print("Você votou no Ciro Gomes!")
        case 13:
            print("Você votou no Lula!")
        case 22:
            print("Você votou no Bolsonaro!")
        case 00: 
            print("Você votou nulo!")
        case _:
            print("O numero digitado não é valido, foi anulado!")



