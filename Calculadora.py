
n1 = int(input('Primeiro Valor'))
n2 = int(input('Segundo Valor'))

opcao = 0

while opcao != 5:
    print ('[1] Soma')
    print ('[2] multiplicação')
    print('[3] Divisão')
    print('[4] Subtração')
    opcao = int(input('Qual é sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}: '.format(n1, n2, soma))
        print('Deseja fazer outra operação?')
    elif opcao == 2:
        multi = n1 * n2
        print('A Multiplicação de {} por {} é: {}: '.format(n1, n2, multi))
    
    elif opcao == 3:
        divisao = n1 / n2
        print('A divisão entre {} e {} é: {}'.format(divisao))
    
    elif opcao == 4:
        subtracao = n1 - n2
        print('A Subtração de {} e {} é :'.format(subtracao))

    elif:
        



