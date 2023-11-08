from random import randint


class Board:

    def __init__(self):
        self.cell_list = []
        for num in range(1, 10):
            self.cell_list.append(Cell(num - 1))
        self.number_filled_cells = 0
        self.initial_board = ['1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9']

    def change_state_of_cell(self, number, symbol):
        if self.cell_list[number - 1].symbol is None:
            self.cell_list[number - 1].change_state(symbol)
            self.number_filled_cells += 1
            return True
        else:
            return False

    def is_game_over(self):
        counter = 0
        for i in range(3):
            if (self.cell_list[i].symbol == self.cell_list[i + 3].symbol
                    and self.cell_list[i].symbol == self.cell_list[i + 6].symbol
                    and self.cell_list[i].symbol is not None):
                return True

            if (self.cell_list[i + counter].symbol == self.cell_list[i + counter + 1].symbol
                    and self.cell_list[i + counter].symbol == self.cell_list[i + counter + 2].symbol
                    and self.cell_list[i + counter].symbol is not None):
                return True
            counter += 2

        if (self.cell_list[0].symbol == self.cell_list[4].symbol
                and self.cell_list[0].symbol == self.cell_list[8].symbol
                and self.cell_list[0].symbol is not None
                or self.cell_list[6].symbol == self.cell_list[4].symbol
                and self.cell_list[6].symbol == self.cell_list[2].symbol
                and self.cell_list[6].symbol is not None):
            return True
        return False

    def draw_board(self, number, symbol):
        self.initial_board[number - 1] = symbol
        self.print_board()

    def print_board(self):
        for i in range(len(self.initial_board)):
            if i == 2 or i == 5:
                print(self.initial_board[i])
            else:
                print(self.initial_board[i], end=' ')
        print()


class Cell:
    is_occupied = False
    symbol = None

    def __init__(self, number):
        self.number = number

    def change_state(self, symbol):
        self.symbol = symbol


class Player:
    number_victories = 0
    player_moves = []

    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number

        self.symbol = '0' if player_number % 2 == 0 else 'X'

    def make_move(self):
        if len(self.player_moves) != 0:
            return self.player_moves[-1]
        else:
            print('Игрок ещё не делал ходы\n')
            return None


class Game:
    state_of_play = -1

    def __init__(self, players, board):
        self.players = players
        self.board = board

    def make_move_game(self, player, board):
        print(f'Ходит {player.name}')
        self.board.print_board()
        while True:
            cell_number = int(input('Введите номер клетки: '))

            if 1 > cell_number or cell_number > 9:
                print('Номера клеток находятся в диапазоне от 1 до 9 включительно\n')
                continue

            elif board.change_state_of_cell(cell_number, player.symbol):
                player.player_moves.append(cell_number)
                board.draw_board(cell_number, player.symbol)
                break

            else:
                print('Клетка занята, попробуйте снова\n')

        player_move = player.make_move()
        print(f'{player.name} поставил {player.symbol} на клетку номер {player_move}\n')
        return board.is_game_over()

    def start_one_game(self):
        self.board = Board()
        player_counter = randint(0, 1)
        while True:
            if self.make_move_game(self.players[player_counter], self.board):
                self.players[player_counter].number_victories += 1
                print(f'Победил {self.players[player_counter].name}\n')
                return True
            elif self.board.number_filled_cells == 9:
                print('Ничья\n')
                return True
            player_counter = (player_counter + 1) % 2

    def main_cycle(self):
        while True:
            self.start_one_game()
            print(f'Текущий счёт:\n'
                  f'{self.players[0].name} {self.players[0].number_victories} : {self.players[1].number_victories} {self.players[1].name}\n')
            print('Если хотите сыграть ещё раз, то введите 1, иначе введите -1')
            action = int(input('Выбор: '))
            print()
            if action == -1:
                break


def main():
    board = Board()
    players = []
    for player_index in range(2):
        symbol = '0' if player_index == 0 else 'X'
        players.append(Player(input(f'Введите имя {player_index + 1}-го игрока (играет за {symbol}): '), player_index))
    print()
    game = Game(players, board)
    game.main_cycle()


main()
