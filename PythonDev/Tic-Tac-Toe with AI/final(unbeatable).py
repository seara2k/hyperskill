import random
import sys


class Table():

    def __init__(self):

        self.template = [[0, 2], [1, 2], [2, 2],
                         [0, 1], [1, 1], [2, 1],
                         [0, 0], [1, 0], [2, 0]]

        self.table = list("         ")

    def show_table(self):
        print("""
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
""".format(*self.table))

    def refresh_win_rows(self):
        self.win_rows = {(0, 1, 2): self.table[:3],
                         (3, 4, 5): self.table[3:6],
                         (6, 7, 8): self.table[6:],
                         (0, 3, 6): self.table[0:7:3],
                         (1, 4, 7): self.table[1:8:3],
                         (2, 5, 8): self.table[2:9:3],
                         (2, 4, 6): self.table[2:7:2],
                         (0, 4, 8): self.table[0:9:4]}

    def find_cell(self, cell):
        true_cell = [int(cell[0]) - 1, int(cell[1]) - 1]
        pos = self.template.index(true_cell)
        return pos

    def place_mark(self, pos):
        if self.table.count("X") == self.table.count("O"):
            self.table[pos] = "X"
        elif self.table.count("X") > self.table.count("O"):
            self.table[pos] = "O"

    def check_winner(self, side):
        if list(side * 3) in self.win_rows.values():
            return True
        elif self.table.count(" ") == 0:
            return None
        else:
            return False


class EasyAI():

    def easy(self, side=None):
        free_cells = [i for i, val in enumerate(self.table) if val == " "]
        random_cell = random.choice(free_cells)
        if side != "medium":
            print("Making move level \"easy\"")
        self.place_mark(random_cell)


class MediumAI():

    def win_or_prevent_win(self, winning_positions):
        for indexes, row in self.win_rows.items():
            if tuple(row) in winning_positions.keys():
                self.place_mark(indexes[winning_positions[tuple(row)]])
                return True

    def medium(self, side):
        x_wins = {("X", "X", " "): 2, ("X", " ", "X"): 1, (" ", "X", "X"): 0}
        o_wins = {("O", "O", " "): 2, ("O", " ", "O"): 1, (" ", "O", "O"): 0}
        print("Making move level \"medium\"")
        if side == "X":
            if self.win_or_prevent_win(x_wins):
                return
            elif self.win_or_prevent_win(o_wins):
                return
        elif side == "O":
            if self.win_or_prevent_win(o_wins):
                return
            elif self.win_or_prevent_win(x_wins):
                return
        self.easy("medium")


class HardAI():

    def hard(self, side):
        self.hardbot = side
        if self.hardbot == "X":
            self.enemy = "O"
        else:
            self.enemy = "X"
        self.function_calls = 0

        self.table_copy = Table()
        self.table_copy.table = self.table[:]
        self.place_mark(self.minimax(self.table_copy, side)[0])

    def minimax(self, table, side, depth=0):
        self.function_calls += 1
        free_cells = [i for i, val in enumerate(table.table) if val == " "]
        table.refresh_win_rows()
        depth += 1
        if table.check_winner(self.hardbot):
            return 10, 10 - depth
        elif table.check_winner(self.enemy):
            return -10, -10 - depth
        elif len(free_cells) == 0:
            return 0, 0

        moves = []

        for i in range(len(free_cells)):
            move_index = free_cells[i]
            table.table[free_cells[i]] = side

            if side == self.hardbot:
                move_score = self.minimax(table, self.enemy, depth)[1]
                move = (move_index, move_score)
            else:
                move_score = self.minimax(table, self.hardbot, depth)[1]
                move = (move_index, move_score)

            table.table[free_cells[i]] = " "
            moves.append(move)
        print(moves)

        if side == self.hardbot:
            best_score = -10000
            for move in moves:
                if move[1] > best_score:
                    best_score = move[1]
                    best_move = move

        else:
            best_score = 10000
            for move in moves:
                if move[1] < best_score:
                    best_score = move[1]
                    best_move = move

        return best_move


class Game(Table, EasyAI, MediumAI, HardAI):

    def __init__(self):
        super(Game, self).__init__()
        self.game_settings()

    def check_main_input(self, command):
        commands = ["start", "easy", "user", "medium", "hard"]
        return set(command) <= set(commands) and len(command) == 3 and command[0] == "start"

    def check_cell_input(self, cell):
        try:
            temp = [int(cell[0]), int(cell[1])]
        except (ValueError, IndexError):
            print("You should enter numbers!")
            return False
        else:
            if (int(cell[0]) > 3 or int(cell[0]) < 1 or int(cell[1]) > 3 or int(cell[1]) < 1):
                print("Coordinates should be from 1 to 3!")
                return False
        return True

    def check_cell(self, pos):

        if self.table[pos] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def user(self, side=None):
        while True:
            input_ = input("Enter the coordinates: ").split()
            if self.check_cell_input(input_):
                pos = self.find_cell(input_)
                if self.check_cell(pos):
                    self.place_mark(pos)
                    break

    def game_settings(self):
        self.table = list("         ")
        self.refresh_win_rows()
        while True:
            input_ = input("Input command: ").split()
            if "exit" in input_:
                break

            elif self.check_main_input(input_):
                input_.remove("start")
                self.game_starts(*input_)
                break
            else:
                print("Bad parameters!")

    def proceed(self, side):
        self.refresh_win_rows()
        self.show_table()
        check_state = self.check_winner(side)
        if check_state:
            print(side + " wins")
            return True
        elif check_state == None:
            print("Draw")
            return True

    def game_starts(self, Xs, Os):
        self.show_table()
        while True:

            getattr(self, Xs)("X")
            if self.proceed("X"):
                break
            getattr(self, Os)("O")
            if self.proceed("O"):
                break
        self.game_settings()


start = Game()
