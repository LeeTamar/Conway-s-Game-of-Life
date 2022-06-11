import numpy as np
import matplotlib.pyplot as plt

class GameOfLife:

    def __init__(self, size_of_board ,board_start_mode = 1 ,rules = "B3/S23" ,rle = "", pattern_position = (0,0)):
        """ init method for class GameOfLife.
        Input size_of_board donates the size of the board, is an integer bigger than 9 and smaller than 1000.
        board_start_mode donates the starting position options, please refer to the added PDF file. Is an integer.
        rules donates the rules of the game. Is a string
        rle: is a str[optional]. the coding for a pattern, if there is an rle coding than the board_start_mode is overlooked,
             if there isn't an rle, than use the board_start_mode.
        pattern_position: is a tuple of two integers (x,y). the upper left position of the pattern on the board,
                          only used if in rle mode.
        Output None.
        """
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        if self.rle == "":  # Sets the starting board, by rle or randomly
            self.pattern_position = (0, 0)
            alive = 255
            dead = 0
            if board_start_mode == 1:
                self.board = np.random.choice([alive, dead], size=(size_of_board, size_of_board)).tolist()
            elif board_start_mode == 2:
                self.board = np.random.choice([alive, alive, alive, alive, dead], size=(size_of_board, size_of_board)).tolist()
            elif board_start_mode == 3:
                self.board = np.random.choice([alive, dead, dead, dead, dead], size=(size_of_board, size_of_board)).tolist()
            elif board_start_mode == 4:
                self.rle = "24bo11b$22bobo11b$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o14b$2o8bo3bob2o4bobo11b$10bo5bo7bo11b$11bo3bo20b$12b2o!"  # להוסיף את ה rle של gospergildergun
                self.pattern_position = (10, 10)
                self.board = self.add_rle_to_pattern_position()
        else:
            self.board = self.add_rle_to_pattern_position()

    def add_rle_to_pattern_position(self):
        """ This method Places the rle on the board in the (x,y) slot according to pattern_position """
        x = self.pattern_position[0]
        y = self.pattern_position[1]
        rle = self.rle
        rle_board = self.transform_rle_to_matrix(rle)
        self.board = np.zeros(([self.size_of_board, self.size_of_board])).tolist()
        row = len(rle_board)
        col = len((rle_board[0]))
        for i in range(x, (x + row)):
            for j in range(y, (y + col)):
                p1 = i - x
                p2 = j - y
                k = rle_board[p1][p2]
                self.board[i][j] = k
        return self.board

    def update(self):
        """ This method updates the board game by the rules of the game. Do a single iteration.
        Input None.
        Output None.
        """
        # Translates the rules into a list of conditions, B - to be born, S - survive
        i = self.rules.find('/')
        B = (list(map(int, list(self.rules[1:i]))))
        S = (list(map(int, list(self.rules[i + 2:]))))
        # update the board
        row = len(self.board)
        col = len((self.board[0]))
        new_board = np.zeros(([row, col])).tolist()
        for i in range(0, row):
            for j in range(0, col):
                L = 0  # סופר תאים חיים
                if 0 < i < (row - 1) and 0 < j < (col - 1):
                    if (self.board[i - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][j + 1]) == 255:
                        L += 1
                elif i == 0 and 0 < j < (col - 1):
                    if (self.board[row - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[row - 1][j]) == 255:
                        L += 1
                    if (self.board[row - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][j + 1]) == 255:
                        L += 1
                elif 0 < i < (row - 1) and j == (col - 1):
                    if (self.board[i - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][0]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][0]) == 255:
                        L += 1
                    if (self.board[i + 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][0]) == 255:
                        L += 1
                elif i == (row - 1) and 0 < j < (col - 1):
                    if (self.board[i - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[0][j - 1]) == 255:
                        L += 1
                    if (self.board[0][j]) == 255:
                        L += 1
                    if (self.board[0][j + 1]) == 255:
                        L += 1
                elif 0 < i < (row - 1) and j == 0:
                    if (self.board[i - 1][col - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][col - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[i + 1][col - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][j + 1]) == 255:
                        L += 1
                elif i == 0 and j == 0:
                    if (self.board[row - 1][col - 1]) == 255:
                        L += 1
                    if (self.board[row - 1][j]) == 255:
                        L += 1
                    if (self.board[row - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][col - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[i + 1][col - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][j + 1]) == 255:
                        L += 1
                elif i == 0 and j == (col - 1):
                    if (self.board[row - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[row - 1][j]) == 255:
                        L += 1
                    if (self.board[row - 1][0]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][0]) == 255:
                        L += 1
                    if (self.board[i + 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i + 1][j]) == 255:
                        L += 1
                    if (self.board[i + 1][0]) == 255:
                        L += 1
                elif i == (row - 1) and j == 0:
                    if (self.board[i - 1][col - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][j + 1]) == 255:
                        L += 1
                    if (self.board[i][col - 1]) == 255:
                        L += 1
                    if (self.board[i][j + 1]) == 255:
                        L += 1
                    if (self.board[0][col - 1]) == 255:
                        L += 1
                    if (self.board[0][j]) == 255:
                        L += 1
                    if (self.board[0][j + 1]) == 255:
                        L += 1
                elif i == (row - 1) and j == (col - 1):
                    if (self.board[i - 1][j - 1]) == 255:
                        L += 1
                    if (self.board[i - 1][j]) == 255:
                        L += 1
                    if (self.board[i - 1][0]) == 255:
                        L += 1
                    if (self.board[i][j - 1]) == 255:
                        L += 1
                    if (self.board[i][0]) == 255:
                        L += 1
                    if (self.board[0][j - 1]) == 255:
                        L += 1
                    if (self.board[0][j]) == 255:
                        L += 1
                    if (self.board[0][0]) == 255:
                        L += 1
                if ((self.board[i][j]) == 0) and L in B:
                    new_board[i][j] = 255
                elif ((self.board[i][j]) == 255) and L in S:
                    new_board[i][j] = 255
                else:
                    new_board[i][j] = 0
        self.board = new_board
        return self.board

    def save_board_to_file(self, file_name):
        """ This method saves the current state of the game to a file. You should use Matplotlib for this.
        Input img_name donates the file name. Is a string, for example file_name = '1000.png'
        Output a file with the name that donates filename.
        """
        plt.imsave(file_name, self.board)

    def display_board(self):
        """ This method displays the current state of the game to the screen. You can use Matplotlib for this.
        Input None.
        Output a figure should be opened and display the board.
        """
        plt.imshow(self.board)  # Showing the board as a picture
        plt.pause(2)  # The time the image will be on the screen

    def return_board(self):
        """ This method returns a list of the board position. The board is a two-dimensional list that every
        cell donates if the cell is dead or alive. Dead will be donated with 0 while alive will be donated with 255.
        Input None.
        Output a list that holds the board with a size of size_of_board*size_of_board.
        """
        return self.board

    def transform_rle_to_matrix(self, rle):
        """ This method transforms an rle coded pattern to a two dimensional list that holds the pattern,
         Dead will be donated with 0 while alive will be donated with 255.
        Input an rle coded string.
        Output a two dimensional list that holds a pattern with a size of the bounding box of the pattern.
        """
        decode_rle = []
        i = 0
        r = 0  # row_count , count $'s
        row_length = 0
        if len(rle) > 0 :
            while i <= (len(rle) - 1):
                a = (list(map(str, list(range(0, 10)))))
                if rle[i] in a:
                    k = i
                    j = i + 1
                    z = rle[i]
                    i = k + 2
                    if rle[j] in a:
                        j = j + 1
                        z = rle[k:j]
                        i = k + 3
                    if rle[j] == 'o':
                        decode_rle.extend([255] * int(z))
                    if rle[j] == 'b':
                        decode_rle.extend([0] * int(z))
                    if rle[j] == '$':
                        r += (int(z) + 1)
                        if row_length == 0:
                            row_length = len(decode_rle)
                        decode_rle.extend([0] * row_length * (int(z)-1))
                elif rle[i] == '$':
                    r += 1
                    i = i + 1
                    if row_length == 0:
                        row_length = len(decode_rle)
                elif rle[i] == 'b':
                    decode_rle.append(0)
                    i = i + 1
                elif rle[i] == 'o':
                    decode_rle.append(255)
                    i = i + 1
                elif rle[i] == '!':
                    r += 1  # כמות השורות
                    l = len(decode_rle)
                    total_length = r * row_length
                    t = total_length - l
                    decode_rle.extend([0] * t)
                    i = i + 1
            rle_as_matrix = [decode_rle[i:i + row_length] for i in range(0, len(decode_rle), row_length)]
        return rle_as_matrix


if __name__ == '__main__':  # You should keep this line for our auto-grading code.
    times = 180
    b = "5b3o11b3o5b$4bo3bo9bo3bo4b$3b2o4bo7bo4b2o3b$2bobob2ob2o5b2ob2obobo2b$b2obo4bob2ob2obo4bob2ob$o4bo3bo2bobo2bo3bo4bo$12bobo12b$2o7b2obobob2o7b2o$12bobo12b$6b3o9b3o6b$6bo3bo9bo6b$6bobo4b3o11b$12bo2bo4b2o5b$15bo11b$11bo3bo11b$11bo3bo11b$15bo11b$12bobo!"
    testing_experience = GameOfLife(size_of_board=100,board_start_mode=4 ,rules="B3/S23", rle=b,pattern_position=(40, 40))
    for i in range(times):
        testing_experience.update()
    testing_experience.display_board()
    print(testing_experience.add_rle_to_pattern_position())
    print('write your tests here')  # don't forget to indent your code here!
