import random   
import os


move_list = ['papel', 'pedra', 'tesoura']
player_count = 0
computer_count = 0

print('================================')
print("Bem vindo ao jogo papel, Pedra e Tesoura")

def main_print():
    print('========================')
    print('\nPlacar:')
    print('Você: {}'.format(player_count))
    print('Computador: {}'.format(computer_count))
    print('\n')
    print('Escolha seu lance:')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')


#Função para que o computador jogue de forma aleatoria
def select_move():
    #retorna um elemento da lista de forma aleatoria.
    return random.choice(move_list) 

#Função do para a pessoa poder jogar
def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            
            return move_list[player_move]

        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count #Transformar a veriavel exclusiva para essa função
    if p_move == 'papel':
        if c_move == "pedra":
            player_count += 1
            return 'p'
        
        elif c_move == "tesoura":
            computer_count += 1
            return 'c'

        else:
            return 'd'
    
    if p_move == 'pedra':
        if c_move == "tesoura":
            player_count += 1
            return 'p'
        
        elif c_move == "papel":
            computer_count += 1
            return 'c'

        else:
            return 'd'

    if p_move == 'tesoura':
        if c_move == "papel":
            player_count += 1
            return 'p'
        
        elif c_move == "pedra":
            computer_count += 1
            return 'c'

        else:
            return 'd'


again = 1
while again == 1: #So sai do lup quando a pessoa não quizer mais jogar.
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print('')
    print('========================')
    print('Sua Jogada: {}'.format(player_move.upper()))
    print('Jogada do computador: {}'.format(computer_move.upper()))

    if winner == 'p':
        print('Você Venceu!')
    elif winner == 'c':
        print('Você perdeu')
    else:
        print('Empate!')
    print('========================')

#Definindo se a pessoa vai continua jogando
    while True:
        print('Jogar Novamente? 0 - SIM  1 - NÃO')
        nex = int(input())
        if nex == 0:
            break
        elif nex == 1:
            again = 0
            break

    os.system('cls')
    


