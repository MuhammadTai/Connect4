import tkinter
import subprocess
import time     #for computer

from tkinter import messagebox
from tkinter import W

from sys import exit
from gameboard import GameBoard
from players import HumanPlayer
from players import ComputerPlayer
from subprocess import call

class Simulator:    #same as GameGUI except there are 2 computer players only
    
    def intialise_dynamic(self):

        
        self.label_1 = tkinter.Label (self.mw, text = "C\nO\nN\nN\nE\nC\nT\n\n4", font = ('Forte 20 bold'), height = 10, width = 3, bg = 'Red', fg = 'Black')

        self.label_1.grid(row =0, column = 8, rowspan = 3, columnspan = 1)  
        
        
        self.label = tkinter.Label(self.mw, text = "S I M U L A T O R", font = ('Haettenschweiler 20'), height = 1, width = 12)
        self.label.grid(row=3, column = 8)
        
        self.button2 = tkinter.Button(self.mw, text = "Restart", font = ('Arial 30 bold'), command = self.restart, height = 2, width = 6) 
        self.button2.grid(row=5, column =8)
        
        for x in range (6):
            for y in range (7):
                self.button = tkinter.Button(self.mw, image = self.default_image, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn(i,j), height= 120 , width = 140, bg ="light blue")
                self.button.grid(row=x, column=y)

                self.buttons_2d_list[x][y] = self.button
        tkinter.mainloop()
    



    def __init__(self):
        

        self.mw = tkinter.Tk()
        self._board = []
        

        
        self.default_image =tkinter.PhotoImage(file = "empty2.gif")  
        
        self.default_image_r = tkinter.PhotoImage(file = "Red2.gif") 
        self.default_image_y = tkinter.PhotoImage(file = "Yellow2.gif")

        
        self.size = 7
        self.buttons_2d_list = []
        for i in range (self.size):
            self.row = [' ']*self.size
            self.buttons_2d_list.append(self.row)
        
        self.gboard = GameBoard(6)
        

        
        p1 = ComputerPlayer ("Y", self.buttons_2d_list) #no input required from user, p1 and p2 are computer players, with given colours
        p2 = ComputerPlayer ("R",self.buttons_2d_list)
            
        print ("\tCLCIK ON ANY BUTTON ON THE GRID TO START")    #the user must click on any button to start the sim

        self.players_lst = (p1, p2)
        self.currnt_player_index = 0
        self.winner = False
        
    def restart (self):
        self.mw.destroy()
        GameGUI.__init__(self)
        GameGUI.intialise_dynamic(self)
        



    def clicked_btn (self,x, y):


        
        p = self.players_lst[self.currnt_player_index]

        button = self.buttons_2d_list[x][y]
        while button["text"] == " " and x < 5:  
                   
            x += 1                              
                                                
            button = self.buttons_2d_list[x][y] 
            
        if button["text"] != " ":               
            x -=1                                
            button = self.buttons_2d_list[x][y] 

            
        
        if button["text"] == " ":
         
            
            button["text"] = p.get_player_circle()  
            
            if p.get_player_circle() == "Y":     
                button = self.buttons_2d_list[x][y]         
                
                
                
                button.configure(image = self.default_image_y)          
                
            elif p.get_player_circle()== "R":
                button = self.buttons_2d_list[x][y]         
           
                button.configure (image = self.default_image_r)           
            self.gboard.make_move(x, y, p.get_player_circle()) 
            

            self.gboard.write_to_file()

            winner = self.gboard.check_winner()

            is_full = self.gboard.is_board_full()
            
            if winner == True:

                win_message = ("Player %s is the Winner!" %p.get_player_circle())
                messagebox.showinfo ("winner Info ", win_message)
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
            p.play()
            






