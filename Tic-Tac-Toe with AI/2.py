import random


class TicTacToeWithAI():

    def __init__(self):
        # self.template = [[[2, 0], [1, 0], [0, 0]],
        #                  [[2, 1], [1, 1], [0, 1]],
        #                  [[2, 2], [1, 2], [0, 2]]]

        # self.temp = [[1, 2, 3],
        #              [4, 5, 6],
        #              [7, 8, 9]]

        self.test = [[0, 2], [1, 2], [2, 2],
                     [0, 1], [1, 1], [2, 1],
                     [0, 0], [1, 0], [2, 0]]

        self.table = list("         ")
        self.refresh_win_rows()

        self.show_table()
        self.game_starts()

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

    def find_cell(self, cell):
        true_cell = [int(cell[0]) - 1, int(cell[1]) - 1]
        pos = self.test.index(true_cell)
        return pos

    def check_cell(self, cell):
        pos = self.find_cell(cell)

        if self.table[pos] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def check_input(self, cell):
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

    def place_mark(self, pos):
        if self.table.count("X") == self.table.count("O"):
            self.table[pos] = "X"
        elif self.table.count("X") > self.table.count("O"):
            self.table[pos] = "O"

    def check_winner(self):

        if list("XXX") in self.win_rows:
            return [True, "X"]
        elif list("OOO") in self.win_rows:
            return [True, "O"]
        if self.table.count(" ") == 0:
            return [False, "Draw"]
        return [False, ""]

    def easy_bot(self):
        free_cells = [i for i, val in enumerate(self.table) if val == " "]
        random_cell = random.choice(free_cells)
        print("Making move level \"easy\"")
        self.place_mark(random_cell)

    def game_starts(self):
        while True:
            print("Enter the coordinates:")
            input_ = input().split()
            if self.check_input(input_) and self.check_cell(input_):
                pos = self.find_cell(input_)
                self.place_mark(pos)
                self.refresh_win_rows()
                self.show_table()
                output = self.check_winner()
                if output[0]:
                    print(output[1] + " wins")
                    break
                else:
                    if output[1] == "Draw":
                        print(output[1])
                        break
                self.easy_bot()
                self.refresh_win_rows()
                self.show_table()
                output = self.check_winner()
                if output[0]:
                    print(output[1] + " wins")
                    break
                else:
                    if output[1] == "Draw":
                        print(output[1])
                        break


lol = TicTacToeWithAI()
