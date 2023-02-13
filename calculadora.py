while True:

    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')

    numeros_validos = None

    try:
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        numeros_validos = True
    except:
        print('Pelo menos um dos números digitados é inválido.')
        continue


    sair = input('Deseja sair? [S]/[N]: ').lower().startswith('s')

    if sair:
        break