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

        self.win_rows = [[0, 1, 2],
                         [3, 4, 5],
                         [6, 7, 8],
                         [0, 3, 6],
                         [1, 4, 7],
                         [2, 5, 8],
                         [2, 4, 6],
                         [0, 4, 8]]
        print("Enter cells:")

        input_ = input().replace("_", " ")

        self.table = list(input_)

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

    def place_mark(self, cell):
        pos = self.find_cell(cell)
        if self.table.count("X") == self.table.count("O"):
            self.table[pos] = "X"
        elif self.table.count("X") > self.table.count("O"):
            self.table[pos] = "O"

    def check_winner(self):
        for row in self.win_rows:
            Xs = 0
            Os = 0
            for item in row:
                if self.table[item] == "X":
                    Xs += 1
                if self.table[item] == "O":
                    Os += 1
            if Xs == 3:
                return [True, "X"]
            elif Os == 3:
                return [True, "O"]
        if self.table.count(" ") == 0:
            return [False, "Draw"]
        return [False, ""]

    def game_starts(self):
        while True:
            print("Enter the coordinates:")
            input_ = input().split()
            if self.check_input(input_) and self.check_cell(input_):
                self.place_mark(input_)
                self.show_table()
                output = self.check_winner()
                if output[0]:
                    print(output[1] + " wins")
                    break
                else:
                    if output[1] == "Draw":
                        print(output[1])
                        break
                    elif output[1] == "":
                        print("Game not finished")
                        break


lol = TicTacToeWithAI()
