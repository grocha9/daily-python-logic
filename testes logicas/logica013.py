import os
import time

cadastro=[
    

]

def limpar_tela():
    os.system('cls')

class Cadastrado:
    def __init__(self, nome, sobrenome, idade, email):
        self.nome=nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.email=email



while True:
    
    print("Central de usuarios")

    print("1-Cadastrar um novo usuario")
    print("2-Listar usuarios cadastrados")
    print("3-Buscar usuario pelo nome")
    print("4-Sair")
    
    try:
        opcao=int(input("Digite sua escolha"))
    except ValueError:
        print("Escreva apenas numeros")
        




    match opcao:
        case 1:
            limpar_tela()
            
            add_nome=input("Nome do cadastrado: ")
            
            add_sobrenome=input("Sobrenome do cadastrado: ")
            try:
                add_idade=int(input("Idade do cadastrado: "))
            except ValueError:
                print("Escreva apenas numeros")
                continue
            
            add_email=input("Email do cadastrado: ")
            
            c1=Cadastrado(add_nome, add_sobrenome, add_idade, add_email)
            
            cadastro.append(c1)
        
        case 2:
            limpar_tela()
            for c in cadastro:
                print(f"Nome:", c.nome, c.sobrenome)
                print(f"Idade: ", c.idade)
                print(f"Email: ", c.email)
                time.sleep(3)
            
        case 3:
            check=False
            limpar_tela()
            busca=input("Qual o nome que você deseja procurar?: ")
            for c in cadastro:
                if busca==c.nome:
                    print("Achamos alguem com esse nome na lista\n")
                    print(f"Nome:", c.nome, c.sobrenome)
                    print(f"Idade: ", c.idade)
                    print(f"Email: ", c.email)
                    check=True
                    break
            if check==False:
                print("Não achamos ninguem na lista com esse nome")
                
        case 4:
            print("Saindo...")
            exit()    
            
        case _:
            print("Digite um numero valido")    
        
