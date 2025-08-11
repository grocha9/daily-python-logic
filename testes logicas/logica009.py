import os

def limpar_tela():
    os.system('cls')


tarefa=[
    
]

class Tarefas:
    def __init__(self, nome, descricao, concluida):
        self.nome=nome
        self.descricao=descricao
        self.concluida = False
    

    
        
while True:
    def painel():
        print("\nPainel de controle das tarefas")
        print("1-Adicionar tarefa")
        print("2-Remover tarefa")
        print("3-Concluir tarefa")
        print("4-Ver tarefas")
        print("5-Sair")
        selecao=int(input("Oque deseja fazer?: "))
        return selecao


    retorno=painel()

    match retorno:
        case 1:
            limpar_tela()
            add_nome=input("Qual o nome da tarefa que deseja adicionar?: ")
            limpar_tela()
            add_desc=input(f"Qual a descrição de {add_nome}: ")
            limpar_tela()        
            
            
            t1= Tarefas(add_nome, add_desc, False)
            tarefa.append(t1)

            
        case 2:
            limpar_tela()
            for t in tarefa:
                print(t.nome, "-", t.descricao)
            remover=int(input("Qual tarefa você quer remover? (1, 2, 3)"))
            remover-=1
            tarefa.pop(remover)
        
        case 3:
            limpar_tela()
            for t in tarefa:
                print(t.nome, "-", t.descricao)
            feito=int(input("Qual tarefa você concluiu? (posição dela na lista)"))
            feito-=1
            tarefa[feito].concluida=True
            
        case 4:
            limpar_tela()
            for t in tarefa:
                if t.concluida:
                            print(f"{t.nome} - {t.descricao} (concluida)")
                else:            
                    print(t.nome, "-", t.descricao)
        
        case 5:
            exit()                
            
            
            
            
        
        
        
        
        
        
