import os
import time
from colorama import Fore, Back, Style, init


class Compras:
    def __init__(self, nome, quantidade):
        self.nome= nome
        self.quantidade= quantidade

lista_compras = []

print(Fore.GREEN + "Bem vindo a lista de compras")
while True:
    print(Style.RESET_ALL+Fore.GREEN + "\n1-Adicionar a lista de compras")
    print(Fore.GREEN + "2-Remover a lista de compras")
    print(Fore.GREEN + "3-Ver lista de compras")
    print(Fore.GREEN + "4-Limpar lista de compras")
    opcao=int(input(Style.BRIGHT + Fore.GREEN + "Digite sua opção: "))

    match opcao:
        case 1:
            os.system('cls')
            compras=input("Qual item você quer adicionar a lista: ")
            quantidade=input("Quantos itens?: ")
            os.system('cls')
            
            
            c1=Compras(compras, quantidade)
            lista_compras.append(c1)
        
        case 2:
            os.system('cls')            
            posicao=1
            for i in lista_compras:
                print(Fore.GREEN + f"\nPosição {posicao}, {i.nome} e você vai comprar {i.quantidade} ")
                posicao+=1
            deletar=int(input("Qual item você deseja deletar? (posição na lista): "))
            os.system('cls')
            deletar-=1
            lista_compras.pop(deletar)
            
        case 3:
            os.system('cls')
            posicao=1
            for i in lista_compras:
                print(Fore.GREEN + f"\nPosição {posicao}, {i.nome} e você vai comprar {i.quantidade} ")
                posicao+=1
        
        case 4:
            os.system('cls')
            lista_compras.clear()
            print(Fore.GREEN + "Lista deletada")
            input("Pressione ENTER para voltar ao menu")
            os.system('cls')
            
        case _:
            os.system('cls')
            print(Fore.RED+"\nInvalido, tente novamente")
    
    
        
    
        
        

