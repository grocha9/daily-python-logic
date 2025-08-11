class Aluno:
    def __init__(self, nome, nota):
        self.nome=nome
        self.nota=nota

nome=input("Digite seu nome: ")
notas = [
    float(input("Digite sua primeira nota: ")),
    float(input("Digite sua segunda nota: ")),
    float(input("Digite sua terceira nota: "))
]

m1=Aluno(nome, 3)

def media_notas(notas):
    media=(notas[0] + notas [1] + notas[2])/3
    media=round (media, 3)
    print(f"{nome}, sua media é {media}")
    
media_notas(notas)
