import random
import os

from matplotlib.pyplot import bar_label

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print('')
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('----------')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('----------')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])

    def reset(self):
        self.board = [[' ', ' ', ' ' ],[' ', ' ', ' '], [' ', ' ', ' ']]
        self.done = ''

    def check_win_or_draw(self):
        dict_win = {}

        for i in ['X', 'O']:
            # Teste de vencedores na horizontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            #TEste de vencedor na vertical
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            #TEste de vencedor na Diagonal
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win['X']:
            self.done = 'X'
            print('X Venceu')
            return

        elif dict_win['O']:
            self.done = 'O'
            print('O Venceu')
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    c += 1
                    break
            
        if c == 0:
            self.done = 'd'
            print('Empate!!')
            return
    
    def make_move(self):
        invalid_move = True

        while invalid_mode:
            try:
                print('Digite a linha do seu proximo lance:')
                x= int(input())

                print('Digite a coluna do seu proximo lance:')
                y= int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas Invalidas')

                if self.board [x] [y] != ' ':
                    print("Posição ja preenchida.")
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_move = False
        self.board[x][y] = 'X'

    
    def make_move(self):
        list_moves =[]

        for i in range(3):
            for j in range[3]:
                if self.board[i][j] == ' ':
                    list_moves.append((i, j))
                
            if len(list_moves) > 0:
                x, y = random.choice(list_moves)
                self.board[x][y] = 'O'




tictactoe = TicTacToe()
tictactoe.print_board()
next = 0

while next == 0:
    os.system('cls')
    tictactoe.print_board()
    while tictactoe == '':
        tictactoe.get_player_move()
        tictactoe.make_move()
        os.system('cls')
        tictactoe.print_board()
        tictactoe.check_win_or_draw()

    print('Digite 1 paea sair do jogo ou qualquer tecla para jogar novamente.')

    next = int(input())
    if next == 1:
        break
    else:
        tictactoe.reset()
        next = 0
        


