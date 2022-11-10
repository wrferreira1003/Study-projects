n1 = int(input('Primeiro Valor'))
n2 = int(input('Segundo Valor'))

opcao = 0

print ('[1] Soma')
print ('[2] multiplicação')
print('[3] Divisão')
print('[4] Subtração')
print('[5] Sair do programa')
opcao = int(input('Qual é sua opção: '))

if opcao == 1:
     soma = n1 + n2
     print('A soma entre {} + {} = {} '.format(n1, n2, soma))
elif opcao == 2:
     multi = n1 * n2
     print('A Multiplicação de {} * {} = {}: '.format(n1, n2, multi))
     
elif opcao == 3:
     divisao = n1 / n2
     print('A divisão entre {} / {} = {}'.format(n1, n2, divisao))
     
elif opcao == 4:
     subtracao = n1 - n2
     print('A Subtração de {} - {} = {}'.format(n1, n2, subtracao))

else:
     print('Opção inválida')



     
