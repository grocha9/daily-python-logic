import random
import time

while True:
    print("Bem vindo ao jogo de impar ou par")
    print("Escolha(impar ou par)")
    escolha=input("")
    if escolha == "impar" or escolha =="par":
        while True:
            print("Escolha um numero")
            numero=float(input(""))
            if numero >=1 and numero <=100:
                numero_computador=random.randint(0,100)
                time.sleep(3)
                print(f"O computador escolheu {numero_computador}")
                soma=numero+numero_computador
                print(f"A soma do seu numero com o do computador é igual {soma}")
                if soma % 2==0:
                    if escolha =="par":
                        print("Parabens você ganhou!!!")
                        exit()
                    else:
                        print("Você perdeu :c")
                        exit()
                else:
                    if escolha =="impar":
                        print("Parabens você ganhou!!!")
                        exit()
                    else:
                        print("Você perdeu :c")
                        exit()
            else:
                print("O seu numero tem que ser de 1 a 100")
    else:
        print("Escolha impar ou par")