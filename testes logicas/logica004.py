import os
import time

while True:

    print("Cofre logico")
    print("Para você abrir esse cofre, tem que inserir a senha correta de 4 numeros, seguindo as pistas (de 0 a 9)")
    
    print("\n\n\nO primeiro digito deve ser impar") #5
    print("\nO segundo digito deve ser maior que o terceiro")#3
    print("\nA soma dos quatro digitos deve ser igual a 20")#2
    print("\nO ultimo digito deve ser igual ao dobro do primeiro")#10
    
    input("\n\n\nPressione Enter para continuar...")
    
    os.system('cls')
    while True:
        print("O primeiro digito deve ser impar") #5
        primeiro=int(input("Digite o primeiro digito do cofre: "))
        
        if primeiro <1 or primeiro > 9:
            print("Numero invalido, tente novamente (1 a 9)")
        else:
            while True:
                print("O segundo digito deve ser maior que o terceiro")
                segundo=int(input("Digite o segundo digito do cofre: "))
                if segundo <1 or segundo >9:
                    print("Numero invalido, tente novamente (1 a 9)")
                else:
                    while True:
                        print("A soma dos quatro digitos deve ser igual a 20")
                        terceiro=int(input("Digite o terceiro digito do cofre: "))
                        if terceiro <1 or terceiro >9:
                            print("Numero invalido, tente novamente (1 a 9)")
                        else:
                            while True:
                                print("O ultimo digito deve ser igual ao dobro do primeiro")
                                quarto=int(input("Digite seu quarto numero: "))
                                if quarto <1 or quarto >9:
                                    print("Numero invalido, tente novamente (1 a 9)")
                                
                                os.system('cls')
                                print(f"Sua senha ficou {primeiro}{segundo}{terceiro}{quarto}")
                                time.sleep(4)

                                if primeiro % 2==0:
                                    print("O primeiro digito do cofre era pra ser impar, mas ele é par")
                                    exit()
                                else:
                                    print("O primeiro numero do cofre é impar, estamos indo bem")
                                    time.sleep(4)
                                    os.system('cls')

                                if segundo > terceiro:
                                    print("O segundo numero é maior que o terceiro, estamos quase abrindo")
                                    time.sleep(4)
                                    os.system('cls')
                                else:
                                    print("O segundo numero não é maior que o terceiro :c")
                                    exit()

                                if primeiro + segundo + terceiro + quarto == 20:
                                    print("A soma dos 4 digitos é 20, estamos com um pé dentro do cofre")
                                    time.sleep(4)
                                    os.system('cls')
                                else:
                                    print("A soma dos 4 digitos não e 20 :c")
                                    exit()

                                if primeiro*2 == quarto:
                                    print("O quarto numero é o dobro do primeiro")
                                    time.sleep(3)
                                    print("Boaaa conseguimos abrir o cadeado!!")
                                    exit()
                                else:
                                    exit()

                                        
                            
                        
                
