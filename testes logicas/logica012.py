import time
import os
from colorama import Fore, Back, Style, init
import random

#🐯 #🍋 #✉️

chance=["✉️","🍋", "🐯" ]

def Giro():
    while True:
        for i in range(20):
            giro1=random.choice(chance)
            giro2=random.choice(chance)
            giro3=random.choice(chance)
            
            os.system('cls')
            print(Style.BRIGHT + Fore.GREEN + "Girando\n")
            print(f"[{giro1}] [{giro2}] [{giro3}]")
            time.sleep(0.15)
        
        if giro1 == "✉️" and giro2 == "✉️" and giro3 == "✉️":
            print(Fore.LIGHTYELLOW_EX+"\nTIGRINHO SOLTOU A CARTA!!!!!")
            input(Fore.LIGHTWHITE_EX+"\nAperte enter para girar novamente")
        elif giro1 == "🐯" and giro2 == "🐯" and giro3 == "🐯":
            print(Fore.LIGHTYELLOW_EX+"\nTIGRINHO TA FORA DA JAULA")
            input(Fore.LIGHTWHITE_EX+"\nAperte enter para girar novamente")
        elif giro1 == "🍋" and giro2 == "🍋" and giro3 == "🍋":
            print(Fore.LIGHTYELLOW_EX+"\nSE A VIDA TE DA LIMÕES, FAÇA UMA LIMONADA")
            input(Fore.LIGHTWHITE_EX+"\nAperte enter para girar novamente")
        else:
            print(Fore.LIGHTRED_EX+"\nVocê perdeu, deve ser porque isso é golpe")
            input(Fore.LIGHTWHITE_EX+"\nAperte enter para girar novamente")
    
Giro()    
