import os

carros = [
        ('Chevrolet Tracker', 120),
        ('Chevrolet Onix', 90),
        ('Chevrolet Spin', 150),
        ('Hyundai HB20', 85),
        ('Hyundai Tucson', 120),
        ('Fiat UNO,', 60),
        ('Fiat Mobi', 70),
        ('Fiat Pulse', 130)
        ]


alugados = []

def mostrar_lista_de_carro(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] {} - R$ {} /dia.'.format(i, car[0], car[1]))



while True:
    os.system("clear") #Função de limpar a tela
    print('==============')
    print('Bem Vindo a Locadora de carros!')
    print('==============')

    print("O que deseja fazer?")
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())

    os.system('clear') #Função de limpar a tela

    if op == 0:
        mostrar_lista_de_carro(carros)

    elif op == 1:
        mostrar_lista_de_carro(carros)
        print('==============')
        print('Escolha o codigo do carro: ')
        cod_car = int(input())
        print('Por quantos dias você deseja alugar este carro?')
        dias = int(input())
        os.system('clear') #Função de limpar a tela

        print('Você escolheu {} por {} dias'.format(carros[cod_car][0], dias))
        print('O Aluguel totalzaria R$ {}. Deseja Alugar?'. format(dias * carros[cod_car][1]))
        
        print('0 - SIM | 1 - NÃO')
        conf = int(input())
        if conf == 0:
            print("Parabens você alugou o {} por {} dias".format(carros[cod_car][0], dias))
            
            #pop extrai o valor e esta inserindo dentro do append, mudando o item de lista
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros alugados. ual você deseja devolver?')
            mostrar_lista_de_carro(alugados)
            print("")
            print('Escolha o código do carro que deseja devolver:')
            cod = int(input())
            if conf == 0:
                print('Obrigado por devolver o carro {}'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))    

    print('')
    print('==============')
    print('DIGITE 0 CONTINUAR | DIGITE 1 PARA SAIR')
    if float(input()) == 1:
        break

