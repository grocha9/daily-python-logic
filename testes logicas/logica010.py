import random
import os

fileira=random.randint(1,5)
coluna=random.randint(1,5)

vidas=10
for tentativas in range (vidas):
    
    
    print("     C1    C2    C3    C4    C5")
    print("F1 (1,1) (1,2) (1,3) (1,4) (1,5)")
    print("F2 (2,1) (2,2) (2,3) (2,4) (2,5)")
    print("F3 (3,1) (3,2) (3,3) (3,4) (3,5)")
    print("F4 (4,1) (4,2) (4,3) (4,4) (4,5)")
    print("F5 (5,1) (5,2) (5,3) (5,4) (5,5)")
    palpite_fi=int(input("Qual fileira você acha que esta o premio: "))
    palpite_co=int(input("Qual coluna você acha que esta o premio: "))



    if palpite_co==coluna and palpite_fi ==fileira:
        print("TEMOS UM VENCEDORRRRRRRRR")
        print("Parabens você ganhou")
        exit()
        
    elif palpite_co < coluna and palpite_fi < fileira:
        os.system('cls')
        print("O tesouro esta mais pra baixo e mais pra direita")
        vidas-=1

    elif palpite_co > coluna and palpite_fi > fileira:
        os.system('cls')
        print("O tesouro esta mais pra cima e mais pra esquerda")
        vidas-=1
        
    elif palpite_co < coluna and palpite_fi > fileira:
        os.system('cls')
        print("O tesouro esta mais pra cima e mais pra direita")
        vidas-=1
        
    elif palpite_co < coluna and palpite_fi == fileira:
        os.system('cls')
        print("Esta na fileira certa, mas na coluna errada, esta mais pra direita")
        vidas-=1
        
    elif palpite_co == coluna and palpite_fi > fileira:
        os.system('cls')
        print("Esta na coluna certa, mas esta na fileira errada, esta mais pra cima")
        vidas-=1
                
    elif palpite_co > coluna and palpite_fi==fileira:
        os.system('cls')
        print("Esta na fileira certa, mas na coluna errada, esta mais pra esquerda")
        vidas-=1
                
    elif palpite_co==coluna and palpite_fi < fileira:
        os.system('cls')
        print("Esta na coluna certa, mas esta na fileira errada, esta mais pra baixo")
        vidas-=1
        
    elif palpite_co > coluna and palpite_fi < fileira:
        os.system('cls')
        print("O tesouro esta mais pra baixo e mais pra direita")
        vidas-=1
    
    else:
        print("Invalido")
