while True:
    tabuada_completa = []
    print("Painel do elevador, qual andar deseja ir?")
    andar=int(input("1 ao 30: "))
    if andar <1 or andar >30:
        print("Coloque um numero valido")
    else:
        for i in range(1, 9):
            linha = i * 4
            tabuada_completa.append(linha)

        if andar in tabuada_completa:
            print(F"O andar {andar} é multiplo de 4, logo ele é proibido")

        elif andar ==13:
            print("O andar 13 não existe, numero do azar")

        else:
            print(f"Subindo para o andar {andar}")
            exit()
