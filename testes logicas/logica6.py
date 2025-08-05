senha=input("Escolha uma senha: ")
tamanho=len (senha)

maiuscula=any(c.isupper() for c in senha)
minuscula=any(c.islower() for c in senha)
numeros=any(c.isdigit() for c in senha)

if tamanho >=8 and maiuscula and minuscula and numeros:
    print("Senha forte")

else:
    print("Senha fraca")