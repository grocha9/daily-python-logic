while True:
    primeiro = float(input("Digite o primeiro número: "))
    segundo = float(input("Digite o segundo número: "))
    terceiro = float(input("Digite o terceiro número: "))

    if primeiro == segundo == terceiro:
        print("Todos os números são iguais")
        break

    elif primeiro <= segundo <= terceiro:
        print(primeiro, segundo, terceiro)
        break
    elif primeiro <= terceiro <= segundo:
        print(primeiro, terceiro, segundo)
        break
    elif segundo <= primeiro <= terceiro:
        print(segundo, primeiro, terceiro)
        break
    elif segundo <= terceiro <= primeiro:
        print(segundo, terceiro, primeiro)
        break
    elif terceiro <= primeiro <= segundo:
        print(terceiro, primeiro, segundo)
        break
    elif terceiro <= segundo <= primeiro:
        print(terceiro, segundo, primeiro)
        break
