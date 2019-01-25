
class GameBoard():     #gamebaord class created

    def __init__(self,s):   #__init__ method defined, 2 parmaters 
        self.__space = ' '  # vaible is declared as a empty space, self used to reference itself

        size_r = 6    #assigning size of board rows (6 rows)
        size_c = 7    #board column (7 columns)


        self.__board = []    #empty list used to store gameboard
        for i in range (6):  #for loop (count-controlled), ensuring i is in range of size
            row = [' '] *size_c   #creating the rows
            self.__board.append(row)    #add row to the end of the gameboard
        

            
    def make_move (self, row, col, element):
        self.__board[row][col] = element     #assign element to the gameboard list which contains a specific row and column value

        
    def get_gameboard(self):    #creating a method which returns the gameboard
        return self.__board
 
    #Below are methods that read the gameboard in order for the computer to decide on what move to make
    
    def cpu_col (self): #all methods that have col in method names refer to columns
                        #these are moves that the human can possibly make
                        #However not all possiblity of moves are covered
                        #These methods are called in the gui file (GameGUI and Difficulty_GameGUI classes)
            
            if self.__board[2][6]  != self.__space: 
                return False            #returns false if the 2nd (3rd) row (from the top) in the 6th (7th) column is empty
            elif self.__board [5][6] == self.__board[4][6] and self.__board[4][6] == self.__board[3][6] != self.__space:    # if the board has 3 discs in the specific column and row that are the same (means player is trying to connect 4), return true
                #print ("3")
                return True

    def cpu_col_1 (self):
            
        if self.__board[1][6] !=self.__space:
           return False 
        elif  self.__board [4][6] == self.__board[3][6] and self.__board[3][6] == self.__board[2][6] != self.__space:
            return True
        
    def cpu_col_2 (self):
            
            if self.__board[2][5] !=self.__space:
                return False
            elif self.__board [5][5] == self.__board[4][5]  and self.__board[4][5] == self.__board[3][5] != self.__space:
                return True
            
    def cpu_col_3 (self):
        
        if self.__board[1][5] !=self.__space:
            return False
        elif  self.__board [4][5] == self.__board[3][5] and self.__board[3][5] == self.__board[2][5] != self.__space:
            return True
        

    def cpu_col_4 (self):
        
        if self.__board[2][4] !=self.__space:
            return False
        elif self.__board [5][4] == self.__board[4][4]  and self.__board[4][4] == self.__board[3][4] != self.__space:
            return True
        
    def cpu_col_5 (self):
        
        if self.__board[1][4] !=self.__space:
            return False
        elif  self.__board [4][4] == self.__board[3][4] and self.__board[3][4] == self.__board[2][4] != self.__space:
            return True
            
    def cpu_col_6 (self):
        
        if self.__board [2][3] !=self.__space:
            return False
        elif self.__board [5][3] == self.__board[4][3]  and self.__board[4][3] == self.__board[3][3] != self.__space:
            return True
        
    def cpu_col_7 (self):
        
        if self.__board[1][3] !=self.__space:
            return False
        elif self.__board [4][3] == self.__board[3][3]  and self.__board[3][3] == self.__board[2][3] != self.__space:
            return True
        
    def cpu_col_8 (self):
        
        if self.__board[2][2] !=self.__space:
            return False
        elif self.__board [5][2] == self.__board[4][2]  and self.__board[4][2] == self.__board[3][2] != self.__space:
            return True

    def cpu_col_9 (self):
    
        if self.__board[1][2] !=self.__space:
            return False
        elif self.__board [4][2] == self.__board[3][2]  and self.__board[3][2] == self.__board[2][2] != self.__space:
            return True

    def cpu_col_10 (self):
        
        if self.__board[2][1] !=self.__space:
            return False
        
        elif self.__board [5][1] == self.__board[4][1]  and self.__board[4][1] == self.__board[3][1] != self.__space:
            return True
            
    def cpu_col_11 (self):
        
        if self.__board[1][1] !=self.__space:
            return False
        
        elif self.__board [4][1] == self.__board[3][1]  and self.__board[3][1] == self.__board[2][1] != self.__space:
            return True
        
    def cpu_col_12 (self):
        
        if self.__board[2][0] !=self.__space:
            return False
        
        elif self.__board [5][0] == self.__board[4][0]  and self.__board[4][0] == self.__board[3][0] != self.__space:
            return True
        
    def cpu_col_13 (self):
        
        if self.__board[1][0] !=self.__space:
            return False
        
        elif self.__board [4][0] == self.__board[3][0]  and self.__board[3][0] == self.__board[2][0] != self.__space:
            return True

    def cpu_col_14 (self):      #this is used so AI can start to connect 4 in column [0]
        if self.__board[1][0] ==self.__space:
            return True

    def cpu_row (self):
        
        if self.__board [5][3] != self.__space:                   #AS LONG AS THE USER DOES NOT ENTER A DISC IN COLUMN 3 THEY CANNOT CONNECT 4 HORIZONTALLY (ROW)
            return False
        elif self.__board [5][6] == self.__board [5][5] and self.__board [5][5] == self.__board[5][4] !=self.__space or self.__board [5][6] == self.__board [5][5] and self.__board [5][5] == self.__board[5][4] !=self.__space or self.__board [5][2] != self.__space or self.__board [5][4] !=self.__space:
            return True

    def cpu_row_1 (self):
        if self.__board [4][3] != self.__space:                   
            return False
        elif self.__board [4][6] == self.__board [4][5] and self.__board [4][5] == self.__board[4][4] !=self.__space or self.__board [4][6] == self.__board [4][5] and self.__board [4][5] == self.__board[4][4] !=self.__space or self.__board [4][2] != self.__space or self.__board [4][4] !=self.__space: 
            return True

    def cpu_row_2 (self):
        if self.__board [3][3] != self.__space:                   
            return False
        elif self.__board [3][6] == self.__board [3][5] and self.__board [3][5] == self.__board[3][4] !=self.__space or self.__board [3][6] == self.__board [3][5] and self.__board [3][5] == self.__board[3][4] !=self.__space or self.__board [3][2] != self.__space or self.__board [3][4] !=self.__space:
            return True

    def cpu_row_3 (self):
        if self.__board [2][3] != self.__space:                   
            return False
        elif self.__board [2][6] == self.__board [2][5] and self.__board [2][5] == self.__board[2][4] !=self.__space or self.__board [2][6] == self.__board [2][5] and self.__board [2][5] == self.__board[2][4] !=self.__space or self.__board [2][2] != self.__space or self.__board [2][4] !=self.__space:
            return True
        
    def cpu_row_4 (self):
        if self.__board [1][3] != self.__space:                   
            return False
        elif self.__board [1][6] == self.__board [1][5] and self.__board [1][5] == self.__board[1][4] !=self.__space or self.__board [1][6] == self.__board [1][5] and self.__board [1][5] == self.__board[1][4] !=self.__space or self.__board [1][2] != self.__space or self.__board [1][4] !=self.__space:
            return True

    def cpu_row_5 (self):
        if self.__board [0][3] != self.__space:                   
            return False
        elif self.__board [0][6] == self.__board [0][5] and self.__board [0][5] == self.__board[0][4] !=self.__space or self.__board [0][6] == self.__board [0][5] and self.__board [0][5] == self.__board[0][4] !=self.__space or self.__board [0][2] != self.__space or self.__board [0][4] !=self.__space :
            return True
    
        
    def cpu_advanced (self):
        if self.__board [3][3] == self.__space:
            return True
    
    #cpu_advanced_2 and _3 can be offensive moves and defensive moves (explained further in Difficulty_GameGUI)
        
    #if the human player tries to connect 4 horizontally in the last row it will be prevented, while the computer tries to connect in the 3rd row

    def cpu_advanced_2 (self):
        if self.__board [5][2] == self.__space and self.__board[5][4] == self.__space:
            return True
        elif self.__board [5][2] != self.__board[5][3] and self.__board[5][3]  != self.__board [5][4] != self.__space:
            return False
        
    def cpu_advanced_3 (self):
        if self.__board[5][2] == self.__space:
            return True
        
    def cpu_advanced_4 (self):
        if self.__board [5][5] !=self.__space:
            return False
        
        elif self.__board [5][2] == self.__board[5][3] and self.__board[5][3]  == self.__board [5][4] != self.__space:
            return True
        
    def cpu_advanced_5(self):
        if self.__board [5][1] !=self.__space:
            return False
        
        elif self.__board [5][2] == self.__board[5][3] and self.__board[5][3]  == self.__board [5][4] != self.__space:
            return True
        
        
    #these methods are used to prevent some possibilities of the human player connecting 4 diagonally
    def cpu_diag (self):
        if self.__board [2][3] != self.__space:
            
            return False
        elif self.__board[5][6] == self.__board[4][5] and self.__board[4][5] == self.__board[3][4] !=self.__space or self.__board[5][0] == self.__board[4][1] and self.__board[4][1] == self.__board[3][2] != self.__space and self.__board[3][3] != self.__space :
            return True

    def cpu_diag_2 (self):
        if self.__board [2][2] != self.__space:
            
            return False
        elif self.__board[5][5] == self.__board[4][4] and self.__board[4][4] == self.__board[3][3] !=self.__space and self.__board[3][2] !=self.__space:
            return True

    def cpu_diag_3 (self):
        if self.__board [2][4] != self.__space:
            
            return False
        elif self.__board[5][1] == self.__board[4][2] and self.__board[4][2] == self.__board[3][3] !=self.__space and self.__board [3][4] !=self.__space:
            return True


    def cpu_diag_4 (self):
        if self.__board [2][5] != self.__space:
            
            return False
        elif self.__board[5][2] == self.__board[4][3] and self.__board[4][3] == self.__board[3][4] !=self.__space and self.__board[3][5] !=self.__space :
            return True        
        
            



    def check_winner(self): #checks the board and players colour, True is returned when player has 4 discs any direction that are the same
        
        
        winner = (self.check_hz()or self.check_vt() or
        #maunually read every position in array to check if 4 spaces have the same pieces diangonally 
        #from top row to bottom right
        (self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2]
        and self.__board[2][2] == self.__board[3][3]  != self.__space or
        
        self.__board[0][1] == self.__board[1][2] and self.__board[1][2] == self.__board[2][3]
        and self.__board[2][3] == self.__board[3][4]  != self.__space or

        self.__board[0][2] == self.__board[1][3] and self.__board[1][3] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][5]  != self.__space or

        self.__board[0][3] == self.__board[1][4] and self.__board[1][4] == self.__board[2][5]
         and self.__board[2][5] == self.__board[3][6]  != self.__space or
        
        self.__board[0][2] == self.__board[1][3] and self.__board[1][3] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][5]  != self.__space or

        #from left column to bottom right
        self.__board[1][0] == self.__board[2][1] and self.__board[2][1] == self.__board[3][2]
         and self.__board[3][2] == self.__board[4][3]  != self.__space or

        self.__board[2][0] == self.__board[3][1] and self.__board[3][1] == self.__board[4][2]
         and self.__board[4][2] == self.__board[5][3]  != self.__space or

        #bottom row to top left
        self.__board[5][6] == self.__board[4][5] and self.__board[4][5] == self.__board[3][4]
         and self.__board[3][4] == self.__board[2][3]  != self.__space or

        self.__board[5][5] == self.__board[4][4] and self.__board[4][4] == self.__board[3][3]
         and self.__board[3][3] == self.__board[2][2]  != self.__space or
        
        self.__board[5][4] == self.__board[4][3] and self.__board[4][3] == self.__board[3][2]
         and self.__board[3][2] == self.__board[2][1]  != self.__space or

        self.__board[5][3] == self.__board[4][2] and self.__board[4][2] == self.__board[3][1]
         and self.__board[3][1] == self.__board[2][0]  != self.__space or

         #from right column to top left and middle diagnols
        self.__board[4][6] == self.__board[3][5] and self.__board[3][5] == self.__board[2][4]
         and self.__board[2][4] == self.__board[1][3]  != self.__space or

        self.__board[4][5] == self.__board[3][4] and self.__board[3][4] == self.__board[2][3]
         and self.__board[2][3] == self.__board[1][2]  != self.__space or
         
        self.__board[4][4] == self.__board[3][3] and self.__board[3][3] == self.__board[2][2]
         and self.__board[2][2] == self.__board[1][1]  != self.__space or

        #from top row to bottom left
        self.__board[0][6] == self.__board[1][5] and self.__board[1][5] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][3]  != self.__space or

        self.__board[0][5] == self.__board[1][4] and self.__board[1][4] == self.__board[2][3]
         and self.__board[2][3] == self.__board[3][2]  != self.__space or

        self.__board[0][4] == self.__board[1][3] and self.__board[1][3] == self.__board[2][2]
         and self.__board[2][2] == self.__board[3][1]  != self.__space or
         
        self.__board[0][3] == self.__board[1][2] and self.__board[1][2] == self.__board[2][1]
         and self.__board[2][1] == self.__board[3][0]  != self.__space or
         
        #left column to top right
         
        self.__board[4][0] == self.__board[3][1] and self.__board[3][1] == self.__board[2][2]
         and self.__board[2][2] == self.__board[1][3]  != self.__space or
        #bottom row to top right
        self.__board[5][0] == self.__board[4][1] and self.__board[4][1] == self.__board[3][2]
         and self.__board[3][2] == self.__board[2][3]  != self.__space or

        self.__board[5][1] == self.__board[4][2] and self.__board[4][2] == self.__board[3][3]
         and self.__board[3][3] == self.__board[2][4]  != self.__space or

        self.__board[5][2] == self.__board[4][3] and self.__board[4][3] == self.__board[3][4]
         and self.__board[3][4] == self.__board[2][5]  != self.__space or
         
        self.__board[5][3] == self.__board[4][4] and self.__board[4][4] == self.__board[3][5]
         and self.__board[3][5] == self.__board[2][6]  != self.__space or

         #middle and remaining diagonals

        self.__board[1][6] == self.__board[2][5] and self.__board[2][5] == self.__board[3][4]
         and self.__board[3][4] == self.__board[4][3]  != self.__space or

        self.__board[1][5] == self.__board[2][4] and self.__board[2][4] == self.__board[3][3]
         and self.__board[3][3] == self.__board[4][2]  != self.__space or

        self.__board[1][4] == self.__board[2][3] and self.__board[2][3] == self.__board[3][2]
         and self.__board[3][2] == self.__board[4][1]  != self.__space))

        

        return winner #if any condition is true, return winner       
                  



    def check_hz (self):    #dynamically check if the board has 4 of the same disc connecting in the rows
        row = ''
        for x in range(6):
            for y in range(7):  #nested for loop in order to reacreate board
                row += self.__board[x][y]   # row is equal to, and added to the board as long as it is in range
            
            if 'YYYY' in row or 'RRRR' in row:  #4 same discs (both colours) in row/board
                return True
            row = ''
        return False

    def check_vt (self):     #dynamically check if the board has 4 of the same disc connecting in the columns
        col = ''
        for y in range (7):
            for x in range (6):
                col += self.__board[x][y]
                
            if 'YYYY' in col or 'RRRR' in col:
                return True
            col =''
        return False

    

        
    
    # the dynamic diagonal check does not work because it the strings concatenate together
    # and the last row is not recognised and only works for half of the board
    """
    def check_bottom_right_to_top_left_corner (self):
        x = 0
        y = 6
        rc = '' #rc is a variable defined as a single string (joins the characters together)
        
        for i in range(12): # amount of loops needed to check board
                
                if (x < 5):
                        
                        rc += GameBoard.move_to_top_left(self,x, y, x)  #must concatenate to get strings
                        x+=1
                    

                else:
                        rc += GameBoard.move_to_top_left(self,x, y, y-1)
                        y-=1
        print("check " + rc)
            
        if 'YYYY' in rc or 'RRRR' in rc: #checking if rc has these strings
            return True
        
    def move_to_top_left (self,x, y, itr):
        rc = ''
        print()
        
        #print("%s " %self.__board[x][y], end = "")
        

        
        for i in range(itr):
            rc += self.__board[x][y]

            x-=1
            y-=1
            
            
            #print("%s " %self.__board[x][y], end = "")
        
        print("tl " + rc)    
        return rc # returning rc for check function
            



     


    def check_bottom_left_to_top_right_corner(self):
        x = 0
        y = 0
        rc = ''
        for i in range (12):    #12 are double the rows
            if (x < 5):
                rc += GameBoard.move_to_top_right(self,x, y, x)
                x +=1 
            else:
                rc += GameBoard.move_to_top_right(self,x, y,(x-y))
                y+=1    #minus works but not adding
        print("check2 " + rc)
        if 'YYYY' in rc or 'RRRR' in rc:
            return True

        
    def move_to_top_right(self,x,y,itr):
        rc = ''       
        print()
        #print("%s " %self.__board[x][y], end = "")

        for i in range(itr):
            
            rc += self.__board[x][y]    #iterate
            x-=1
            y+=1
            
            #print("%s " %self.__board[x][y], end = "")
        print("tr " + rc)

        return rc
        

    """
        
        

    def is_board_full(self):    #a method that checks if all spaces are empty
        row = ''
        for x in range (6): # x is rows, y is columns
            for  y in range (7):
                row += self.__board[x][y]   #row is equal to and added to 42 times

            if ' ' in row:
                return False
            row = ''
        return True
    
    def is_board_full_small(self):  #method used to check for empty spaces on a smaller board (-2 in rows and columns from standard board)
        row =''
        for x in range (6-2):
            for y in range (7-2):
                row += self.__board[x][y]   
            if ' ' in row:
                return False
            row = ''
        return True


    def is_space_free (self, row, col):
        
        if self.__board[row][col] == " ":

            return True
        return False
    


            
    def write_to_file(self):    # write the board array to a text file
        print()
        print("%s " %self.__board, end ="")
        file_name = "Connect4_Saves.txt"
        file = open(file_name, "w") #open file in wite mode
        file.write("")
        file.write("%s " %self.__board) #write board as a string
        file.close()    #close file

       

    
class Large_gameboard():    #all the methods are the same as the GameBoard class except the board has 2 additional rows and columns
    

    def __init__(self,s): #__init__ function defined, 2 parmaters 
        self.__space = ' '  # vraible is declared as a empty space
        
        size_r = 6+2    #assigning size of board rows
        size_c = 7+2 #board column
        
        """
        self.__board = [list(" "*7)for i in range (6)]   #empty board"""
        self.__board = []
        for i in range (7+2):  #for loop (count-controlled), ensuring i is in range of size
            row = [' '] *size_c   #creating the rows
            self.__board.append(row)

            

    def make_move (self, row, col, element):
        self.__board[row][col] = element     #the player should only be able to choose coloum, not row



    def check_winner(self): #checks the board and players colour, True is returned when player has won

        winner = (self.check_hz()or self.check_vt()or
        #maunually read every position in array to check if 4 spaces have the same pieces diangonally 
        # from top row to bottom right
        #adding two extra rows and columns
        (self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2]
        and self.__board[2][2] == self.__board[3][3]  != self.__space or
        
        self.__board[0][1] == self.__board[1][2] and self.__board[1][2] == self.__board[2][3]
        and self.__board[2][3] == self.__board[3][4]  != self.__space or

        self.__board[0][2] == self.__board[1][3] and self.__board[1][3] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][5]  != self.__space or

        self.__board[0][3] == self.__board[1][4] and self.__board[1][4] == self.__board[2][5]
         and self.__board[2][5] == self.__board[3][6]  != self.__space or
        
        self.__board[0][2] == self.__board[1][3] and self.__board[1][3] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][5]  != self.__space or

        #from left column to bottom right
        self.__board[1][0] == self.__board[2][1] and self.__board[2][1] == self.__board[3][2]
         and self.__board[3][2] == self.__board[4][3]  != self.__space or

        self.__board[2][0] == self.__board[3][1] and self.__board[3][1] == self.__board[4][2]
         and self.__board[4][2] == self.__board[5][3]  != self.__space or

        #bottom row to top left
        self.__board[5][6] == self.__board[4][5] and self.__board[4][5] == self.__board[3][4]
         and self.__board[3][4] == self.__board[2][3]  != self.__space or

        self.__board[5][5] == self.__board[4][4] and self.__board[4][4] == self.__board[3][3]
         and self.__board[3][3] == self.__board[2][2]  != self.__space or
        
        self.__board[5][4] == self.__board[4][3] and self.__board[4][3] == self.__board[3][2]
         and self.__board[3][2] == self.__board[2][1]  != self.__space or

        self.__board[5][3] == self.__board[4][2] and self.__board[4][2] == self.__board[3][1]
         and self.__board[3][1] == self.__board[2][0]  != self.__space or

         #from right column to top left and middle diagnols
        self.__board[4][6] == self.__board[3][5] and self.__board[3][5] == self.__board[2][4]
         and self.__board[2][4] == self.__board[1][3]  != self.__space or

        self.__board[4][5] == self.__board[3][4] and self.__board[3][4] == self.__board[2][3]
         and self.__board[2][3] == self.__board[1][2]  != self.__space or
         
        self.__board[4][4] == self.__board[3][3] and self.__board[3][3] == self.__board[2][2]
         and self.__board[2][2] == self.__board[1][1]  != self.__space or

        #from top row to bottom left
        self.__board[0][6] == self.__board[1][5] and self.__board[1][5] == self.__board[2][4]
         and self.__board[2][4] == self.__board[3][3]  != self.__space or

        self.__board[0][5] == self.__board[1][4] and self.__board[1][4] == self.__board[2][3]
         and self.__board[2][3] == self.__board[3][2]  != self.__space or

        self.__board[0][4] == self.__board[1][3] and self.__board[1][3] == self.__board[2][2]
         and self.__board[2][2] == self.__board[3][1]  != self.__space or
         
        self.__board[0][3] == self.__board[1][2] and self.__board[1][2] == self.__board[2][1]
         and self.__board[2][1] == self.__board[3][0]  != self.__space or
         
        #left column to top right
         
        self.__board[4][0] == self.__board[3][1] and self.__board[3][1] == self.__board[2][2]
         and self.__board[2][2] == self.__board[1][3]  != self.__space or
        #bottom row to top right
        self.__board[5][0] == self.__board[4][1] and self.__board[4][1] == self.__board[3][2]
         and self.__board[3][2] == self.__board[2][3]  != self.__space or

        self.__board[5][1] == self.__board[4][2] and self.__board[4][2] == self.__board[3][3]
         and self.__board[3][3] == self.__board[2][4]  != self.__space or

        self.__board[5][2] == self.__board[4][3] and self.__board[4][3] == self.__board[3][4]
         and self.__board[3][4] == self.__board[2][5]  != self.__space or
         
        self.__board[5][3] == self.__board[4][4] and self.__board[4][4] == self.__board[3][5]
         and self.__board[3][5] == self.__board[2][6]  != self.__space or

         #middle and remaining diagnols

        self.__board[1][6] == self.__board[2][5] and self.__board[2][5] == self.__board[3][4]
         and self.__board[3][4] == self.__board[4][3]  != self.__space or

        self.__board[1][5] == self.__board[2][4] and self.__board[2][4] == self.__board[3][3]
         and self.__board[3][3] == self.__board[4][2]  != self.__space or

        self.__board[1][4] == self.__board[2][3] and self.__board[2][3] == self.__board[3][2]
         and self.__board[3][2] == self.__board[4][1]  != self.__space or
                  
        #the extra rows and coloumns for the large board
        #bottom row to top left
        self.__board[7][8] == self.__board[6][7] and self.__board[6][7] == self.__board[5][6]
         and self.__board[5][6] == self.__board[4][5]  != self.__space or

        self.__board[6][7] == self.__board[5][6] and self.__board[5][6] == self.__board[4][5]
         and self.__board[4][5] == self.__board[3][4]  != self.__space or
         
        self.__board[7][7] == self.__board[6][6] and self.__board[5][5] == self.__board[4][4]
         and self.__board[4][4] == self.__board[3][3]  != self.__space or

        self.__board[6][6] == self.__board[5][5] and self.__board[4][4] == self.__board[3][3]
         and self.__board[3][3] == self.__board[2][2]  != self.__space or

        self.__board[7][6] == self.__board[6][5] and self.__board[6][5] == self.__board[5][4]
         and self.__board[5][4] == self.__board[4][3]  != self.__space or
         
        self.__board[6][5] == self.__board[5][4] and self.__board[5][4] == self.__board[4][3]
         and self.__board[4][3] == self.__board[3][2]  != self.__space or
         
        self.__board[7][5] == self.__board[6][4] and self.__board[6][4] == self.__board[5][3]
         and self.__board[5][3] == self.__board[4][2]  != self.__space or

        self.__board[6][4] == self.__board[5][3] and self.__board[5][3] == self.__board[4][2]
         and self.__board[4][2] == self.__board[3][1]  != self.__space or

        self.__board[7][4] == self.__board[6][3] and self.__board[6][3] == self.__board[5][2]
         and self.__board[5][2] == self.__board[4][1]  != self.__space or

        self.__board[6][3] == self.__board[5][2] and self.__board[5][2] == self.__board[4][1]
         and self.__board[4][1] == self.__board[3][0]  != self.__space or

        self.__board[7][3] == self.__board[6][2] and self.__board[6][2] == self.__board[5][1]
         and self.__board[5][1] == self.__board[4][0]  != self.__space or 
         
        self.__board[7][0] == self.__board[6][1] and self.__board[6][1] == self.__board[5][2]
         and self.__board[5][2] == self.__board[4][3]  != self.__space or
    
         # bottom row to top right
        self.__board[6][0] == self.__board[5][1] and self.__board[5][1] == self.__board[4][2]
         and self.__board[4][2] == self.__board[3][3]  != self.__space or

        self.__board[6][1] == self.__board[5][2] and self.__board[5][2] == self.__board[4][3]
         and self.__board[4][3] == self.__board[3][3]  != self.__space or

        self.__board[7][1] == self.__board[6][2] and self.__board[6][2] == self.__board[5][3]
         and self.__board[4][4] == self.__board[3][5]  != self.__space or

        self.__board[6][2] ==self.__board[6][2] and self.__board[6][2] == self.__board[5][3]
         and self.__board[5][3] == self.__board[4][4]  != self.__space or
         
        self.__board[7][2] == self.__board[6][3] and self.__board[6][3] == self.__board[5][4]
         and self.__board[5][4] == self.__board[4][5]  != self.__space or
         
        self.__board[6][3] == self.__board[5][4] and self.__board[5][4] == self.__board[4][5]
         and self.__board[4][5] == self.__board[3][6]  != self.__space or

        self.__board[7][3] == self.__board[6][4] and self.__board[6][4] == self.__board[5][5]
         and self.__board[5][5] == self.__board[4][6]  != self.__space or

        self.__board[6][4] == self.__board[5][5] and self.__board[5][5] == self.__board[4][6]
         and self.__board[4][6] == self.__board[3][7]  != self.__space or
         
        self.__board[7][4] == self.__board[6][5] and self.__board[6][5] == self.__board[5][6]
         and self.__board[5][6] == self.__board[4][7]  != self.__space or

        self.__board[6][5] == self.__board[5][6] and self.__board[5][6] == self.__board[4][7]
         and self.__board[4][7] == self.__board[3][8]  != self.__space or

        self.__board[7][5] == self.__board[6][6] and self.__board[6][6] == self.__board[5][7]
         and self.__board[5][7] == self.__board[4][8]  != self.__space or

         #right column to top left

        self.__board[6][8] == self.__board[5][7] and self.__board[5][7] == self.__board[4][6]
         and self.__board[4][6] == self.__board[3][5]  != self.__space or

        self.__board[5][7] == self.__board[4][6] and self.__board[4][6] == self.__board[3][5]
         and self.__board[3][5] == self.__board[2][4]  != self.__space or

        self.__board[5][8] == self.__board[4][7] and self.__board[4][7] == self.__board[3][6]
         and self.__board[3][6] == self.__board[2][5]  != self.__space or

        self.__board[4][7] == self.__board[3][6] and self.__board[3][6] == self.__board[2][5]
         and self.__board[2][5] == self.__board[1][4]  != self.__space or

        self.__board[4][8] == self.__board[3][7] and self.__board[3][7] == self.__board[2][6]
         and self.__board[2][6] == self.__board[1][5]  != self.__space or

        self.__board[3][7] == self.__board[2][6] and self.__board[2][6] == self.__board[1][5]
         and self.__board[1][5] == self.__board[0][4]  != self.__space or

        self.__board[3][8] == self.__board[2][7] and self.__board[2][7] == self.__board[1][6]
         and self.__board[1][6] == self.__board[0][5]  != self.__space or

         #right column to bottom left

        self.__board[0][8] == self.__board[6][6] and self.__board[6][6] == self.__board[5][7]
         and self.__board[5][7] == self.__board[4][8]  != self.__space or

        self.__board[1][7] == self.__board[2][6] and self.__board[2][6] == self.__board[3][5]
         and self.__board[3][5] == self.__board[4][4]  != self.__space or

        self.__board[1][8] == self.__board[2][7] and self.__board[2][7] == self.__board[3][6]
         and self.__board[3][6] == self.__board[4][5]  != self.__space or

        self.__board[2][7] == self.__board[3][6] and self.__board[3][6] == self.__board[4][5]
         and self.__board[4][5] == self.__board[5][4]  != self.__space or

        self.__board[2][8] == self.__board[3][7] and self.__board[3][7] == self.__board[4][6]
         and self.__board[4][6] == self.__board[5][5]  != self.__space or

        self.__board[3][7] == self.__board[4][6] and self.__board[4][6] == self.__board[5][5]
         and self.__board[5][5] == self.__board[6][4]  != self.__space or

        self.__board[3][8] == self.__board[4][7] and self.__board[4][7] == self.__board[5][6]
         and self.__board[5][6] == self.__board[6][5]  != self.__space or

        self.__board[4][7] == self.__board[5][6] and self.__board[5][6] == self.__board[6][5]
         and self.__board[6][5] == self.__board[7][4]  != self.__space or

        self.__board[4][8] == self.__board[5][7] and self.__board[5][7] == self.__board[6][6]
         and self.__board[6][6] == self.__board[7][5]  != self.__space))
         
        return winner
        
                  
   


    def check_hz (self):
        row = ''
        for x in range(6+2):
            for y in range(7+2):
                row += self.__board[x][y]
                
            if 'YYYY' in row or 'RRRR' in row:
                return True
            row = ''
        return False

    def check_vt (self):
        col = ''
        for y in range (7+2):
            for x in range (6+2):
                col += self.__board[x][y]
                
            if 'YYYY' in col or 'RRRR' in col:
                return True
            col =''
        return False
   

    

        
        

    def is_board_full(self):
        row = ''
        for x in range (6+2): # x is rows, y is columns
            for  y in range (7+2):
                row += self.__board[x][y]

            if ' ' in row:
                return False
            row = ''
        return True

    def is_space_free (self, row, col):

        
        if self.__board[row][col] == " ":

            return True
        return False
    


            
    def write_to_file(self):
        print()
        print("%s " %self.__board, end ="")
        file_name = "Connect4_Saves.txt"
        file = open(file_name, "w")
        file.write("")
        file.write("%s " %self.__board)
        file.close()
        
    
