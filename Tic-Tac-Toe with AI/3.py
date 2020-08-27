import random


class TicTacToeWithAI():

    def __init__(self):

        self.template = [[0, 2], [1, 2], [2, 2],
                         [0, 1], [1, 1], [2, 1],
                         [0, 0], [1, 0], [2, 0]]

        self.table = list("         ")

        self.game_settings()

    def show_table(self):
        print("""
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
""".format(*self.table))

    def refresh_win_rows(self):
        self.win_rows = [self.table[:3],
                         self.table[3:6],
                         self.table[6:],
                         self.table[0:7:3],
                         self.table[1:8:3],
                         self.table[2:9:3],
                         self.table[2:7:2],
                         self.table[0:9:4]]

    def check_main_input(self, command):
        commands = ["start", "easy", "user"]
        return set(command) <= set(commands) and len(command) == 3

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

    def find_cell(self, cell):
        true_cell = [int(cell[0]) - 1, int(cell[1]) - 1]
        pos = self.template.index(true_cell)
        return pos

    def check_cell(self, pos):

        if self.table[pos] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def place_mark(self, pos):
        if self.table.count("X") == self.table.count("O"):
            self.table[pos] = "X"
        elif self.table.count("X") > self.table.count("O"):
            self.table[pos] = "O"

    def check_winner(self):

        if list("XXX") in self.win_rows:
            print("X wins")
        elif list("OOO") in self.win_rows:
            print("O wins")
        elif self.table.count(" ") == 0:
            print("Draw")
        else:
            return True

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

    def user(self):
        while True:
            input_ = input("Enter the coordinates: ").split()
            if self.check_cell_input(input_):
                pos = self.find_cell(input_)
                if self.check_cell(pos):
                    self.place_mark(pos)
                    break

    def easy(self):
        free_cells = [i for i, val in enumerate(self.table) if val == " "]
        random_cell = random.choice(free_cells)
        print("Making move level \"easy\"")
        self.place_mark(random_cell)

    def proceed(self):
        self.refresh_win_rows()
        self.show_table()
        if not self.check_winner():
            return True

    def game_starts(self, Xs, Os):
        self.show_table()
        while True:

            getattr(self, Xs)()
            if self.proceed():
                break
            getattr(self, Os)()
            if self.proceed():
                break
        self.game_settings()


lol = TicTacToeWithAI()
