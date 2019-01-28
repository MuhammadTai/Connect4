import tkinter  # used for the GUI of connect 4 game
import subprocess
import time     #for computer player and animations
from tkinter import messagebox #display end game messages such as winner/draw
import os
import ast

from sys import exit    #used to exit game
from gameboard import GameBoard     #importing all the necessary classes from files
from players import HumanPlayer
from players import ComputerPlayer
from subprocess import call
from gameboard import Large_gameboard



class GameGUI:
    load = False;
    leave = False;
        
    def intialise_dynamic(self):
        
        
        self.label_1 = tkinter.Label (self.mw, text = "C\nO\nN\nN\nE\nC\nT\n\n4", font = ('Forte 20 bold'), height = 10, width = 3, bg = 'Red', fg = 'Black') # creating a lable that will dislay connect 4 at the right side of the gameboard

        self.label_1.grid(row =0, column = 8, rowspan = 3, columnspan = 1)  #span takes aways the grid size limitation
                                                                            #giving location of label 1
        
        p = self.players_lst[self.currnt_player_index]      # used to display in another label which player is the current player
        
        self.label = tkinter.Label(self.mw, text = "Player %s turn " %p.get_player_circle(), font = ('Arial 11 bold'), height = 1, width = 10)
        self.label.grid(row=3, column = 8)
        
        self.button2 = tkinter.Button(self.mw, text = "Restart", font = ('Arial 30 bold'), command = self.restart, height = 2, width = 6) #restart button, command calls the restart method
        self.button2.grid(row=5, column =8)

        #self.hover = tkinter.Label (self.mw, text = "111")
        #self.hover2 = tkinter.Label (self.mw, text = "222")
        #self.hover.grid(row

        # Creating the connect 4 GUI grid, which consist of buttons in a grid
        for x in range (6):
            for y in range (7):

                # storing the deafult image (from __init__ method) and empty text spaces in all buttons within the grid/loop

                self.button = tkinter.Button(self.mw, image = self.default_image, text = " ", font = ('Arial 30 bold'),
                                             command = lambda i = x, j = y: self.clicked_btn(i,j), height= 120 , width = 140, bg ="light blue") #the command (lambda) retrieves the x and y values and runs the clicked_btn method for every button
                self.button.grid(row=x, column=y)   #assigning x and y to the grid row and column, .grid creates the grid of buttons

                def on_enter(event, button=self.button):
                    button['background'] = 'green'
                    x, y = button.winfo_rootx(), button.winfo_rooty()
                    print(x,y)

                def on_leave(event, button=self.button):
                    button['background'] = 'white'

                
                self.button.bind("<Enter>",on_enter)
                self.button.bind("<Leave>",on_leave)

                
                self.buttons_2d_list[x][y] = self.button    #buttons assigned to list



                def loading(button):  #reading the text file to create the board saved in the text file
                        #this method does not work (index error)
        
                    #self.load = True; #to see if the user wants the saved game

                    print(self.load);
                    
                    self._board = self.gboard.get_gameboard()
                    try:
                        file = open ("Connect4_Saves.txt", "r") #open file
                    
                    except FileNotFoundError:

                        print("\n\n\tSave File is not found!\n\n\tYou need to play a game, or the last game was already finished\n")
                        self.leave = True;
                        return;
                                            
                    #button = self.buttons_2d_list[0][5]
                    #print(button)
                    for line in file:
                        line = ast.literal_eval(line)  #read file as a list
                        for i in range (6):
                            diff = 0;
                            for j in range(7):
                                #print(line[5][y])
                                self._board[i][j] = line[i][j]
                                if (line[i][j]!= " " and button["text"] == " " and  x == i and y == j):
                                        button["text"]=line[i][j] 
                                        self.gboard.make_move(i, j, line[i][j])
                                        print(button)
                                        if (line[i][j] == "Y"):
                                            button.configure(image = self.default_image_y)

                                        if(line[i][j] == "R"):
                                            button.configure(image = self.default_image_r)
                                        
                                elif (x == 5 and y == 6 ):   #if the gui loop has finished
                                    self.load = False;
                                            
                        
                                  
                    file.close()

                
                if (self.leave == True):
                    return

                if (self.load == True): 
                    loading(button =self.button)
           
            
        
        
        tkinter.mainloop()  #an infinite loop, runs until window is destroyed
    

 

        
    def __init__(self):
        
        
        self.mw = tkinter.Tk()  #assigning the GUI method Tk to variable self.mw

        # default image = black hole/empty space
        self.default_image =tkinter.PhotoImage(file = "empty2.gif")  #all buttons will start with this deafult image when game starts and need to make instance so tkinter does keeps image
        # red and yellow represent the disc colours
        self.default_image_r = tkinter.PhotoImage(file = "Red2.gif") #IMPORTANT TO MAKE INSTANCE OF ALL IMAGES IN __INIT__ METHOD TO PREVENT IMAGES FROM DISAPPAERING 
        self.default_image_y = tkinter.PhotoImage(file = "Yellow2.gif")

        
        self.size = 7
        self.buttons_2d_list = []
        for i in range (self.size):
            self.row = [' ']*self.size
            self.buttons_2d_list.append(self.row)   #creating a button list in order to configure mechanics of the game nad game GUI
        
        self.gboard = GameBoard(6)  #gameboard reference

        
        print ("\tYELLOW or RED")   
        colour = input ("Please Select Your Colour(y/r): ") #giving user option to select colour
        colour = colour.lower()
        if colour == "y":
            p1 = HumanPlayer ("Y")  #assigning colours to variables p1 and p2
            p2 = ComputerPlayer ("R",self.buttons_2d_list)
            opnt = input ("\t Do you want to play against a computer(y/n)? ")
            if opnt == "y":
                p2 = ComputerPlayer ("R", self.buttons_2d_list)
            
            else :
                p2 = HumanPlayer ("R")
            

        else:
            p1 = HumanPlayer("R")
            p2 = ComputerPlayer ("Y",self.buttons_2d_list)
            opnt = input ("\t Do you want to play against a computer(y/n)? ")
            if opnt == "y":
                    p2 = ComputerPlayer ("Y", self.buttons_2d_list)
                    
            else :
                    p2 = HumanPlayer ("Y")
            
        

        self.players_lst = (p1, p2) # creating a list of the players
        self.currnt_player_index = 0 #initilise the current player to zero
        self.winner = False #initilise winner to false


        
        
    def restart (self): #restart the board and the __init__ method
        self.mw.destroy()   #.destroy destroys the GUI window
        GameGUI.__init__(self)
        GameGUI.intialise_dynamic(self)
        
    


    def clicked_btn (self,x, y):
        
        """
        print(x, y)"""

        
        p = self.players_lst[self.currnt_player_index]
        
        button = self.buttons_2d_list[x][y]
        print (button)
        
        while button["text"] == " " and x < 5:  # while loop(runs as many times until condtion is false), while button is empty and the row is less than 5,
                                                #the grid rows start from 0 at the top and ends at 5 at the bottom
                
            x += 1                              # x is incremented by 1 until it reaches 4,
                                                # althogh last row it stops at 4, the loop will choose the row below the button selected
            button = self.buttons_2d_list[x][y] # after the loop has reached the last empty row is will implement the button in array
            
        if button["text"] != " ":               #if space is not empty in row
            x -=1                               #decrement (go 1 up in grid) by 1 to select the next empty space 
            button = self.buttons_2d_list[x][y] #button is implemented once empty space is found in row
        

   
        if button["text"] == " ":
         
            
            button["text"] = p.get_player_circle()  #place player circle in
            
            if p.get_player_circle() == "Y":     #chnaged for loop to while
                a = 0;
                button = self.buttons_2d_list[x][y]         #gives location of move  
                animation = self.buttons_2d_list[a][y]
                
                if p.get_name() == "Computer Player":
                    self.currnt_player_index = 0 #set the next player turn, in order to prevent human player to take the computers turn during the pause
                    self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                    self.mw.after(2000)    ###### SHOW THE AI MOVE AFTER 2 SECS

                    while a < x:
                        animation = self.buttons_2d_list[a][y]
                        animation.configure(image = self.default_image_y)
                        self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                        self.mw.after(500)    ###### SHOW THE AI MOVE AFTER .5 SEC
                        animation.configure(image = self.default_image)
                        self.mw.update()
                        a += 1;
                    
                    button.configure(image = self.default_image_y)
                    self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                    self.currnt_player_index = 1
                    
                else:
                    
                    while a < x:
                        animation = self.buttons_2d_list[a][y]
                        animation.configure(image = self.default_image_y)
                        self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                        self.mw.after(500)    ###### SHOW THE AI MOVE AFTER .5 SEC
                        animation.configure(image = self.default_image)
                        self.mw.update()
                        a += 1;

                    button.configure(image = self.default_image_y)          #changing the image in the button from black to yellowe
                    
                
            elif p.get_player_circle()== "R":
                a = 0;
                button = self.buttons_2d_list[x][y]         #gives location of move
                animation = self.buttons_2d_list[a][y]


            
                if p.get_name() == "Computer Player":
                    self.currnt_player_index = 0 #set the next player turn to computer, in order to prevent human player to take the computers turn during the pause
                    
                    self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                    self.mw.after(2000)    ###### SHOW THE AI MOVE AFTER 2 SECS
                    ### ANIMATION

                    while a < x:
                        animation = self.buttons_2d_list[a][y]
                        animation.configure(image = self.default_image_r)
                        self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                        self.mw.after(500)    ###### SHOW THE AI MOVE AFTER .5 SEC
                        animation.configure(image = self.default_image)
                        self.mw.update()
                        a += 1;


                    
                    button.configure (image = self.default_image_r)
                    self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                    self.currnt_player_index = 1
                    
                else:
                    
                    while a < x:
                        animation = self.buttons_2d_list[a][y]
                        animation.configure(image = self.default_image_r)
                        self.mw.update()    ###### FORCES GUI TO UPDATE , THIS REMOVES THE FREEZING EFFECT
                        self.mw.after(500)    ###### SHOW THE AI MOVE AFTER .5 SEC
                        animation.configure(image = self.default_image)
                        self.mw.update()
                        a += 1;

                    button.configure (image = self.default_image_r) #change image from black to yellow
               
   
            
            
            self.gboard.make_move(x, y, p.get_player_circle()) #move
            
            
                
            
            self.gboard.write_to_file() #if game if exited half way or winner is announced the gameboard is written to a text file

            winner = self.gboard.check_winner() 

            is_full = self.gboard.is_board_full()
            
            if winner == True:          #condition of winner
                os.remove("Connect4_Saves.txt")
                if p.get_player_circle() == "Y":
                    win_message = ("Yellow Player is the Winner!" )
                else:
                    win_message = ("Red Player is the Winner!" )
                
                messagebox.showinfo ("Winner Info ", win_message)
                self.mw.destroy()
                return

            elif is_full == True:
                os.remove("Connect4_Saves.txt")
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                return      #return back to elif loop in game_menu, display pause() print statement
                

                
            else:
                pass #if no winner or board is not full, carry on playing

            if self.currnt_player_index == 1:   #a turn based player index
                self.currnt_player_index = 0    #p2 (human player) is = 1, p1 (computer player) is = 0
                                                #if p2 has taken turn(== 1), change to p1 ( = 0)
            else:                               

                self.currnt_player_index += 1    #after human player has taken turn, return back to computer by incrementing by 1
            
    
            p = self.players_lst[self.currnt_player_index]  # assigning current player to the variable p

            

            # these are moves used by the medium difficulty AI - alothough no choice was give to user to select difficulty in this class - medium is default
            # if user wants to change difficulty, the game menu lets you change difficulty
            # these moves prevent human player connect 4 in rows and columns (not all)
            # this also lets the AI connect 4 if the certain codition met
            if self.gboard.cpu_col() or self.gboard.cpu_col_1() == True and p.get_name() == "Computer Player" : #condition
                
                p.ai()  #move
                
            elif self.gboard.cpu_col_2() or self.gboard.cpu_col_3() == True and p.get_name () == "Computer Player": 
                p.ai_1 ()
                
            elif self.gboard.cpu_col_4() or self.gboard.cpu_col_5() == True and p.get_name () == "Computer Player":
               p.ai_2 ()

            elif self.gboard.cpu_col_6() or self.gboard.cpu_col_7() == True and p.get_name () == "Computer Player":
               p.ai_3 ()
               
            elif self.gboard.cpu_col_8() or self.gboard.cpu_col_9() == True and p.get_name () == "Computer Player":
               p.ai_4 ()
               
            elif self.gboard.cpu_col_10() or self.gboard.cpu_col_11() == True and p.get_name () == "Computer Player":
               p.ai_5 ()

            elif self.gboard.cpu_col_12() or self.gboard.cpu_col_13() == True and p.get_name () == "Computer Player" :
                p.ai_6()
               
            elif self.gboard.cpu_row() or self.gboard.cpu_row_1() or self.gboard.cpu_row_2() or self.gboard.cpu_row_3() or self.gboard.cpu_row_4() or self.gboard.cpu_row_5() == True:
                p.ai_3()

            elif self.gboard.cpu_col_14() == True and p.get_name () == "Computer Player" :   #techniques used to connect 4 in first column
                p.ai_6()
            
            else:
                p.play()    #random moves if no conditions are met
            


    #async comp():
        
                
class Difficulty_GameGUI: #similar methods to previous class except added difficulty 

    def intialise_dynamic(self):    #same as initilise_dynamic in GameGUI class

        
        self.label_1 = tkinter.Label (self.mw, text = "C\nO\nN\nN\nE\nC\nT\n\n4", font = ('Forte 20 bold'), height = 10, width = 3, bg = 'Red', fg = 'Black')
        """
        self.label_1.tag_add("red", "1.0", "1.4")
        self.label_1.tag_config("red", foreground="red")"""
        self.label_1.grid(row =0, column = 8, rowspan = 3, columnspan = 1)  
        
        p = self.players_lst[self.currnt_player_index]
        self.label = tkinter.Label(self.mw, text = "You are Colour %s" %p.get_player_circle(), font = ('Arial 11 bold'), height = 1, width = 10)
        self.label.grid(row=3, column = 8)
        
        self.button2 = tkinter.Button(self.mw, text = "Restart", font = ('Arial 30 bold'), command = self.restart_difficulty, height = 2, width = 6)  
        self.button2.grid(row=5, column =8)
        
        for x in range (6):
            for y in range (7):
                self.button = tkinter.Button(self.mw, image = self.default_image, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn(i,j), height= 120 , width = 140, bg ="light blue")
                self.button.grid(row=x, column=y)
                """
                self.button.grid_forget()"""
                self.buttons_2d_list[x][y] = self.button
        tkinter.mainloop()
    




        
    def __init__(self):
        

        self.mw = tkinter.Tk()
    
        

        
        self.default_image =tkinter.PhotoImage(file = "empty2.gif")  
        
        self.default_image_r = tkinter.PhotoImage(file = "Red2.gif") 
        self.default_image_y = tkinter.PhotoImage(file = "Yellow2.gif")

        
        self.size = 7
        self.buttons_2d_list = []
        for i in range (self.size):
            self.row = [' ']*self.size
            self.buttons_2d_list.append(self.row)
        
        self.gboard = GameBoard(6)
        d = input ("\nSelect Difficulty: Easy(e) - Medium (default)(m) - Advanced (a) > ")  # giving the user the option to slect between 3 difficulties
        d = d.lower()
            
        print ("\tYELLOW or RED")
        colour = input ("Please Select Your Colour(y/r) : ")   #no need to ask user if they want to play aginst computer
        colour = colour.lower()
        if colour == "y":
            p1 = HumanPlayer ("Y")
            p2 = ComputerPlayer ("R",self.buttons_2d_list)
            

        else:
            
            p1 = HumanPlayer("R")
            p2 = ComputerPlayer ("Y",self.buttons_2d_list)
      
        self.difficulty = d  #assigning the input given to the variable 'd' to self.difficulty
        self.players_lst = (p1, p2)
        self.currnt_player_index = 0
        self.winner = False

    def loading(self):
        self._board = self.gboard.get_gameboard()   
        
        file = open ("Connect4_Saves.txt", "r")
        for r_1 in range (6):
            line = file.readline()
            self._board[r_1][0] = line[0]
            self._board[r_1][1] = line[1]
            self._board[r_1][2] = line[2]
            self._board[r_1][3] = line[3]
            self._board[r_1][4] = line[4]
            self._board[r_1][5] = line[5]
            
            print(line)
        file.close()
        
    def restart_difficulty (self):
        self.mw.destroy()
        Difficulty_GameGUI.__init__(self)
        Difficulty_GameGUI.intialise_dynamic(self)
        
    


    def clicked_btn (self,x, y):
        

        
        p = self.players_lst[self.currnt_player_index]
        
        button = self.buttons_2d_list[x][y]
        animation = self.buttons_2d_list[x][y]
        
        while button["text"] == " " and x < 5:  #last row is 5


            x += 1                              #move the disc down
                                                
            button = self.buttons_2d_list[x][y] 
            
        if button["text"] != " ":               
            x -=1                               #move disc up
            button = self.buttons_2d_list[x][y] 
        

     
        if button["text"] == " ":
         
            
            button["text"] = p.get_player_circle()  
            
            if p.get_player_circle() == "Y":     
                button = self.buttons_2d_list[x][y]         
                
                
                
                button.configure(image = self.default_image_y)          
                
            elif p.get_player_circle()== "R":
                button = self.buttons_2d_list[x][y]         

                button.configure (image = self.default_image_r)
               
            if p.get_name() == "Computer Player":
                time.sleep(2)
                print ("Thinking...") 
                self.gboard.make_move(x, y, p.get_player_circle())
            else:
            
                self.gboard.make_move(x, y, p.get_player_circle()) 
                


            
            
            self.gboard.write_to_file()

            winner = self.gboard.check_winner()

            is_full = self.gboard.is_board_full()
            
            if winner == True:
                if p.get_player_circle() == "Y":
                    win_message = ("Yellow Player is the Winner!" )
                else:
                    win_message = ("Red Player is the Winner!" )
                
                messagebox.showinfo ("Winner Info ", win_message)
                self.mw.destroy()
                return

            elif is_full == True:
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                return      
                

                
            else:
                pass

            if self.currnt_player_index == 1:
                self.currnt_player_index = 0
            else:

                self.currnt_player_index += 1
            
    
            p = self.players_lst[self.currnt_player_index]
            
            if self.difficulty == "e":  #if input was from user was 'e' the random computer player moves will be used
                p.play()
                
            elif self.difficulty == "m":    #if input was 'm' the same conditions and statements are used in the default connect 4 game (previous class) 
                
                if self.gboard.cpu_col() or self.gboard.cpu_col_1() == True and p.get_name() == "Computer Player" :
                    
                    
                    p.ai()
                
                elif self.gboard.cpu_col_2() or self.gboard.cpu_col_3() == True and p.get_name () == "Computer Player": #can use OR to call same function twice usefull to make cpu connect 4
                    p.ai_1 ()
                
                elif self.gboard.cpu_col_4() or self.gboard.cpu_col_5() == True and p.get_name () == "Computer Player":
                    p.ai_2 ()

                elif self.gboard.cpu_col_6() or self.gboard.cpu_col_7() == True and p.get_name () == "Computer Player":
                   p.ai_3 ()
               
                elif self.gboard.cpu_col_8() or self.gboard.cpu_col_9() == True and p.get_name () == "Computer Player":
                   p.ai_4 ()
               
                elif self.gboard.cpu_col_10() or self.gboard.cpu_col_11() == True and p.get_name () == "Computer Player":
                   p.ai_5 ()
                elif self.gboard.cpu_row_12() or self.gboard.cpu_col_13() == True and p.get_name () == "Computer Player":
                    p.ai_6()
               
                elif self.gboard.cpu_row() or self.gboard.cpu_row_1() or self.gboard.cpu_row_2() or self.gboard.cpu_row_3() or self.gboard.cpu_row_4() or self.gboard.cpu_row_5() == True:
                    p.ai_3()

                elif self.gboard.cpu_col_14() == True and p.get_name () == "Computer Player" :  
                    p.ai_6()
                    
                else:
                    p.play()
                    
            elif self.difficulty == "a":    #if user enters 'a' the advanced computer will be used
                                            #the avanced uses the same techniques as the medium ai, however more conditions and improvements are made 

                
                # these functions make computer player block attempts of human player connecting 4
                if self.gboard.cpu_col() or self.gboard.cpu_col_1() == True and p.get_name() == "Computer Player" : #
                    #self.currnt_player_index ==1
                    print ("7")
                    p.ai()
                
                elif self.gboard.cpu_col_2() or self.gboard.cpu_col_3() == True and p.get_name () == "Computer Player": 
                    p.ai_1 ()
                
                elif self.gboard.cpu_col_4() or self.gboard.cpu_col_5() == True and p.get_name () == "Computer Player":
                    p.ai_2 ()

                elif self.gboard.cpu_col_6() or self.gboard.cpu_col_7() == True and p.get_name () == "Computer Player":
                   p.ai_3 ()
               
                elif self.gboard.cpu_col_8() or self.gboard.cpu_col_9() == True and p.get_name () == "Computer Player":
                   p.ai_4 ()
               
                elif self.gboard.cpu_col_10() or self.gboard.cpu_col_11() == True and p.get_name () == "Computer Player":
                   p.ai_5 ()
                elif self.gboard.cpu_col_12() or self.gboard.cpu_col_13() == True and p.get_name () == "Computer Player" :
                    p.ai_6()
                elif self.gboard.cpu_row() or self.gboard.cpu_row_1() or self.gboard.cpu_row_2() or self.gboard.cpu_row_3() or self.gboard.cpu_row_4() or self.gboard.cpu_row_5() == True:
                    p.ai_3()
                    
                #the computer player trying to connect 4
                elif self.gboard.cpu_advanced() == True and p.get_name() == "Computer Player":   #best first move as it eliminates users chances of connecting 4 horizontally
                                                                                                 #the ai enters its move in the middle column making it challenging for the human player to connect 4 horizantally
                                                                                                 #the ai also prevents the user from winning vertically and diagnoally in some areas
                    p.ai_3()
                    
                # cpu_advanced_2 and cpu_advanced_ 3 are offensive and defensive moves
                # the AI will instantly try to connect 4 in the middle (4th) column
                # based on opponents moves it decides moves to make (highest priority is to prevent human from winning)
                #if the human user blocks this attempt the computer player will try to connect 4 horizontally in the bottom row
                elif self.gboard.cpu_advanced_2() == True and p.get_name() == "Computer Player":
                    p.ai_2()

                elif self.gboard.cpu_advanced_3() == True and p.get_name() == "Computer Player":
                    p.ai_4()

                elif self.gboard.cpu_advanced_4() == True and p.get_name() == "Computer Player":
                    p.ai_1()
                            
                elif self.gboard.cpu_advanced_5() == True and p.get_name() == "Computer Player":
                    p.ai_5()
                    
                
                elif self.gboard.cpu_diag() == True and p.get_name () == "Computer Player":
                    p.ai_3 ()

                elif self.gboard.cpu_col_14() == True and p.get_name () == "Computer Player" :
                    p.ai_6()
        
                else:
                    p.play()

                #the AI still needs alot more improvement as these are limited possibilities/conditions


                    
            else:
                print ("")
                print("Enter a correct choice")
                self.mw.destroy()   #destor if user enters incorrect value/character

                
            


 
            






class Grid_mode:    #same methods as previous classes, except diffrent grid sizes
    
    def small_grid(self):
        self.label_1 = tkinter.Label (self.mw, text = "C\nO\nN\nN\nE\nC\nT\n\n4", font = ('Forte 20 bold'), height = 10, width = 3, bg = 'Red', fg = 'Black')
        self.label_1.grid(row =0, column = 8-2, rowspan = 3, columnspan = 1)  

        
        self.button2 = tkinter.Button(self.mw, text = "Restart", font = ('Arial 30 bold'), command = self.restart_small, height = 2, width = 6) 
        self.button2.grid(row=5-2, column =8-2)
        
        for x in range (6-2):   #smaller grid (-2)
            for y in range (7-2):
                self.button = tkinter.Button(self.mw, image = self.default_image, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn_2(i,j), height= 120 , width = 140, bg ="light blue")
                self.button.grid(row=x, column=y)

                self.buttons_2d_list[x][y] = self.button
        tkinter.mainloop()
        
    def large_grid(self):
        self.label_1 = tkinter.Label (self.mw, text = "C\nO\nN\nN\nE\nC\nT\n\n4", font = ('Forte 20 bold'), height = 10, width = 3, bg = 'Red', fg = 'Black')
        self.label_1.grid(row =0, column = 8+2, rowspan = 3+2, columnspan = 1) 

        
        self.button2 = tkinter.Button(self.mw, text = "Restart", font = ('Arial 30 bold'), command = self.restart_large, height = 1, width = 6) #restart button 
        self.button2.grid(row=5+2, column =8+2)
        
        for x in range (6+2):   #larger grid (+2)
            for y in range (7+2):
                self.button = tkinter.Button(self.mw, image = self.default_image_2, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn_3(i,j), height= 80 , width = 100, bg ="light blue") # smaller buttons to hold smaller images and too fit grid in window
                self.button.grid(row=x, column=y)
                """
                self.button.grid_forget()"""
                self.buttons_2d_list[x][y] = self.button
        tkinter.mainloop()

    def __init__(self):
        

        self.mw = tkinter.Tk()
        self._board = []
        

        self.default_image =tkinter.PhotoImage(file = "empty2.gif")     
        self.default_image_2 =tkinter.PhotoImage(file = "empty3.gif")  #instead of using the same images, as used in the standard board.
                                                                       #I had to reduce the size of the images in order to fit the window of the larger
        
        self.default_image_r = tkinter.PhotoImage(file = "Red2.gif")    # I created another set of images
        self.default_image_r_2 = tkinter.PhotoImage(file = "Red3.gif")
        self.default_image_y_2 = tkinter.PhotoImage(file = "Yellow3.gif")
        self.default_image_y = tkinter.PhotoImage(file = "Yellow2.gif")

        
        self.size = 7+2
        self.buttons_2d_list = []
        for i in range (self.size):
            self.row = [' ']*self.size
            self.buttons_2d_list.append(self.row)
        
        self.gboard = Large_gameboard(6+2)      #calling the largest gameboard
    
        print ("\tYELLOW or RED")
        colour = input ("Please Select Your Colour(y/r): ")
        colour = colour.lower()
        if colour == "y":
            p1 = HumanPlayer ("Y")
            p2 = ComputerPlayer ("R",self.buttons_2d_list)
            opnt = input ("\t Do you want to play against a computer(y/n)? ")
            if opnt == "y":
                p2 = ComputerPlayer ("R", self.buttons_2d_list)
               
            else :
                p2 = HumanPlayer ("R")
            
            
        
        else:
            p1 = HumanPlayer("R")
            p2 = ComputerPlayer ("Y",self.buttons_2d_list)
            opnt = input ("\t Do you want to play against a computer(y/n)? ")
            if opnt == "y":
                    p2 = ComputerPlayer ("R", self.buttons_2d_list)
                   
            else :
                    p2 = HumanPlayer ("Y")
            
        
        
        self.players_lst = (p1, p2)
        self.currnt_player_index = 0
        self.winner = False
        
    def restart_small (self):
        self.mw.destroy()
        Grid_mode.__init__(self)   
        Grid_mode.small_grid(self)
        
    def restart_large (self):
        self.mw.destroy()
        Grid_mode.__init__(self)    
        Grid_mode.large_grid(self)
        



        
    def clicked_btn_2 (self,x, y): # used for the small grid
        

        p = self.players_lst[self.currnt_player_index]

        button = self.buttons_2d_list[x][y]
        while button["text"] == " " and x < 5 - 2:  
                                             
                       
            x += 1                              
                                                
            button = self.buttons_2d_list[x][y]
            
        if button["text"] != " ":               
            x -=1                                
            button = self.buttons_2d_list[x][y] 
            
        if button["text"] == " ":
            
            button["text"] = p.get_player_circle()  
            
            self.gboard.make_move(x, y, p.get_player_circle()) 

            if p.get_player_circle() == "Y":     
                button = self.buttons_2d_list[x][y]         
               
                
                
                button.configure(image = self.default_image_y)         
                
            elif p.get_player_circle()== "R":
                button = self.buttons_2d_list[x][y]         

                button.configure (image = self.default_image_r)
            if p.get_name() == "Computer Player":
                time.sleep(2)
                print ("Thinking...") 
                self.gboard.make_move(x, y, p.get_player_circle()) 
            else:
            
                self.gboard.make_move(x, y, p.get_player_circle()) 
   
            winner = self.gboard.check_winner()

            is_full = self.gboard.is_board_full()

            if winner == True:

                win_message = ("Player %s is the Winner!" %p.get_player_circle())
                messagebox.showinfo ("Winner Info ", win_message)
                self.mw.destroy()
                return 

            elif is_full == True:
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                return      
                
            else:
                pass

            if self.currnt_player_index == 1:
                self.currnt_player_index = 0
            else:
                self.currnt_player_index += 1
            

            p = self.players_lst[self.currnt_player_index]
            p.play_small()  #the small grid only has an AI that is easy difficulty (random moves only)



            
    def clicked_btn_3 (self,x, y): # used for the large grid
        

        p = self.players_lst[self.currnt_player_index]

        button = self.buttons_2d_list[x][y]
        while button["text"] == " " and x < 5 + 2:  
                                            
                    
            x += 1                              
                                                
            button = self.buttons_2d_list[x][y]
            
        if button["text"] != " ":               
            x -=1                               
            button = self.buttons_2d_list[x][y] 
            
        if button["text"] == " ":
            
            button["text"] = p.get_player_circle()  
            
            self.gboard.make_move(x, y, p.get_player_circle()) 

            if p.get_player_circle() == "Y":     
                button = self.buttons_2d_list[x][y]         
                
                
                
                button.configure(image = self.default_image_y_2)          
                
            elif p.get_player_circle()== "R":
                button = self.buttons_2d_list[x][y]        
 
                button.configure (image = self.default_image_r_2)
            if p.get_name() == "Computer Player":
                time.sleep(2)
                print ("Thinking...") 
                self.gboard.make_move(x, y, p.get_player_circle()) 
            else:
            
                self.gboard.make_move(x, y, p.get_player_circle()) 
            

            winner = self.gboard.check_winner()

            is_full = self.gboard.is_board_full()

            if winner == True:

                win_message = ("Player %s is the Winner!" %p.get_player_circle())
                messagebox.showinfo ("Winner Info ", win_message)
                self.mw.destroy()
                return 

            elif is_full == True:
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                return      
                
            else:
                pass

            if self.currnt_player_index == 1:
                self.currnt_player_index = 0
            else:
                self.currnt_player_index += 1
            

            p = self.players_lst[self.currnt_player_index]

           
             

            p.play_large() #the large grid only has an AI that is easy difficulty (random moves only)
  
                
        
