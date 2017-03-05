import random
import os
import sys
import time
from msvcrt import getch

class game_life:
    def __init__ (self, height = 10, width = 15, prob = 0.5, max_moves = 100):
        self.height = height
        self.width = width
        self.prob = prob
        self.max_moves = max_moves
        ## random.seed(123)
        self.game_field = [[1 if (random.random()<prob) else 0 for y in range(width)] for x in range(height)] 
        
    ## Count number of neighbours for the cell
    def count_neighbours (self, i,j):
        all_neighb = [self.game_field[(i+m) % self.height][(j+k) % self.width] for m in range(-1,2) for k in range(-1,2)]
        return sum(all_neighb) - all_neighb[4]
    
    ## Check if the cell survived
    def check_survive (self, i,j):
        new_status = self.game_field[i][j]
        if self.neighb_count[i][j]<2: ## underpopulation 
            new_status = 0
        elif self.neighb_count[i][j]>3: ## overpopulation
            new_status = 0
        elif self.neighb_count[i][j]==3:
            new_status = 1
        return new_status
        
    ## Make single game move
    def next_move (self):
        self.neighb_count = [[self.count_neighbours(x,y) for y in range(self.width)] for x in range(self.height)] 
        self.game_field = [[self.check_survive(x,y) for y in range(self.width)] for x in range(self.height)] 
        pass
    
    ## Print game field
    def print_states(self):
        ## [print(self.game_field[x]) for x in range(self.height)]
        [print("".join("* " if (self.game_field[x][y]==1) else "  " for y in range(self.width))) for x in range(self.height)]        
        pass
    
    ## Play whole game
    def play_game(self):
        for i in range(self.max_moves):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("time passed: ", i,"\n")
            self.print_states()
            self.next_move()
            time.sleep(0.5)
        pass


if __name__ == "__main__":
    user_args = [10,15,0.3] ## default_args
    try:
       user_args[0] = int(sys.argv[1])  
       user_args[1] = int(sys.argv[2])  
       user_args[2] = float(sys.argv[3])  
    except:
        pass

    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Welcome to the Conway's Game of Life")
    print ("\nProvided arguments:")
    print ("field height:",user_args[0])
    print ("field width:",user_args[1])
    print ("Initial birth probability:",user_args[2])
    print ("\nPress any key to start")
    getch()
    tt = game_life(height = user_args[0], width = user_args[1], prob = user_args[2])
    tt.play_game()