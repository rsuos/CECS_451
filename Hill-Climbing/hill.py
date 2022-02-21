# Ryan Suos
# Hill Climbing
import copy
import time
from board import *

def queen_dictionary(self):
    queens = {}

    row = 0
    queenNumber = 1
    for x in self.map:
        index = 0
        for y in x:
            if (y == 1):
                queens[queenNumber] = [row, index]
                queenNumber += 1
            index += 1
        row = row + 1
    return queens

def hill_climbing(self):
    
    queens = queen_dictionary(self)
    best_fit = self
    
    for queen in queens:
        queen_position = queens.get(queen)
        x = queen_position[0]
        y = queen_position[1]

        # Sections:
        # 1|2|3
        # 4|Q|5
        # 6|7|8
        
        # Section 1
        if ( x - 1 in range(len(self.map)) and y - 1 in range(len(self.map[0]))):
            if (self.map[x-1][y-1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x-1), (y-1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 2
        if ( x - 1 in range(len(self.map)) and y in range(len(self.map[0]))):
            if (self.map[x-1][y] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x-1), (y))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 3
        if ( x - 1 in range(len(self.map)) and y + 1 in range(len(self.map[0]))):
            if (self.map[x-1][y+1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x-1), (y+1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 4
        if ( x in range(len(self.map)) and y - 1 in range(len(self.map[0]))):
            if (self.map[x][y-1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x), (y-1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 5
        if ( x in range(len(self.map)) and y + 1 in range(len(self.map[0]))):
            if (self.map[x][y+1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x), (y+1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 6
        if ( x + 1 in range(len(self.map)) and y - 1 in range(len(self.map[0]))):
            if (self.map[x+1][y-1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x+1), (y-1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 7
        if ( x + 1 in range(len(self.map)) and y in range(len(self.map[0]))):
            if (self.map[x+1][y] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x+1), (y))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
        # Section 8
        if ( x + 1 in range(len(self.map)) and y + 1 in range(len(self.map[0]))):
            if (self.map[x+1][y+1] == 0):
                test_case = copy.deepcopy(self)
                test_case.flip((x+1), (y+1))
                test_case.flip(x, y)
                if (test_case.get_fitness() < best_fit.get_fitness()):
                    best_fit = test_case
    return best_fit
    
def restart():
    return Board(5)

# Main Function    
board = Board(5)

start_time = time.time()

board = hill_climbing(board)
while (board.get_fitness() != 0):
    board = restart()
    board = hill_climbing(board)
finish_time = round((time.time() - start_time) * 1000)

print("Running time: %ims" % finish_time)
for i in range(len(board.map)):
    for j in range(len(board.map[0])):
        if (board.map[i][j] == 1):
            print(1, end =" ")
        else:
            print('-', end =" ")
    print("")
