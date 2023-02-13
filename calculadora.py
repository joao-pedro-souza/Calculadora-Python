while True:

    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operacao = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)
        numeros_validos = True
    except:
        print('Pelo menos um dos números digitados é inválido.')
        continue

    if len(operacao) > 1:
        print('Digite apenas um operador.')
        continue

    if operacao not in '+-/*':
        print('Operador inválido')
        continue

    sair = input('Deseja sair? [S]/[N]: ').lower().startswith('s')

    if sair:
        break