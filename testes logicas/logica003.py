number=int(input("Me fale um numero INTEIRO: "))

if number % 3 == 0 and number % 5 == 0:
    print("Numero magico!!!")
elif number % 3 ==0:
    print("Três é o charme!!")
elif number % 5 ==0:
    print("Cinco estrelas!!")

else:
    print("Apenas um numero comum por aqui")
    
