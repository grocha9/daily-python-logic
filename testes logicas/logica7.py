import time
import random

class personagem:
    def __init__(self, nome, vida, defesa):
        self.nome=nome
        self.vida=vida
        self.defesa=defesa

        

def escolha():
    while True:
        print("Bola de fogo, dano 30")
        print("Raio, de dano 20")
        ataque=input("Quer começar usando qual habilidade?").lower()
        if ataque=="bola de fogo":
            print("Você taca uma bola de fogo nele, causando 30 de dano")
            vilão.vida-=(30-vilão.defesa)
        elif ataque=="raio":
            print("Cai um raio na cabeca do vilão, causando 20 de dano")
            vilão.vida-=(20-vilão.defesa)
        if vilão.vida<=0:
            print("O vilão morreu parabens")
            exit()
        else:
            print(f"o vilão aida tem {vilão.vida}/100")
            
        rando=random.randint(1,2)
        if rando==1:
            print("O vilão taca uma chama negra em você causando 20 de dano")
            heroi.vida-=(20-heroi.defesa)
        elif rando==2:
            print("O vilão puxa um cajado magico e te ataca com ele, causando 10 de dano")
            heroi.vida-=(10-heroi.defesa)
        if heroi.vida<= 0:
            print("Você morreu :c")
            exit()
        else:
            print(f"Voce ainda tem {heroi.vida} restante")
        
        
         
heroi= personagem("Heroi", 100, 5)
vilão= personagem("Vilão", 100, 5)
    
print("Você encontra o vilão que perseguia a seculos, e vocês travam uma batalha MORTAL")
time.sleep(3)
escolha()

