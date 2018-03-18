class Player:       #creating a player superclass
    
    def __init__(self,colour):    
        self.circle = colour    #Initialize circle attribute (instance variable)
        
                                    #Accessors for player class data attribute
    def get_player_circle(self):    #initialise get_player_circle with self parameter
        return self.circle  #calling players circle



class HumanPlayer(Player):  #A Human player with paramater of Player class (subclass)

    def __init__(self, colour):
        Player.__init__(self, colour)
        self.name = "Human Player"
    
    def play(self):
        pass    #no code required for playing
                #human player is free to make their own moves
    def ai(self):
        pass
    def ai_1(self):
        pass
    def ai_2(self):
        pass
    def ai_3(self):
        pass
    def ai_4(self):
        pass
    def ai_5(self):
        pass
    def ai_6(self):
        pass
    def ai_new(self):
        pass
    def get_name (self):
        return self.name
    def play_small(self):
        pass
    def play_large(self):
        pass
    def ai_a(self):
        pass
        

import random   #usign libary function 'import' to call 'random' module which generates random numbers
import time     #creating a time delay in computer player
from gameboard import GameBoard

class ComputerPlayer(Player):
    
    def __init__(self, colour, buttns_list):
        Player.__init__(self, colour)
        self.buttons_2d_list = buttns_list
        self.name = "Computer Player"
        self.__space = ' '
        
        self.gboard = GameBoard(6)

        
    # using techniques to connect 4 and prevent human from winning
    def get_name(self):
        return self.name    #method that creates that returns who the current player is
    # below are methods that are used by the computer in onder to place discs in the gameboard
    def play(self):
        
        
        is_space_free = False   #assign is_space_free as a False (not) value

        while (is_space_free == False): #while loop, while variable is equal to false procceed to print statement

            
            print ("Player %s turn" %self.get_player_circle())  #informing user on players turn
            # the cpu will make moves randomly 
        
        
            r = random.randint (0,5)    #assign random integer as a variable 'r' , and interger between or equal to 0 and 5
                                        
            c = random.randint (0,6)    

            self.button = self.buttons_2d_list[r][c]    #initialise 'button' attribute to button list with r and c
            
            is_space_free = self.button["text"] == " "  #checking if the button has an empty space
            
        self.button.invoke()    #invokes the tkinter button
        
    def ai (self):
        is_space_free = False   
        
        if (is_space_free == False): 
          
            
            
            print ("Player %s turn" %self.get_player_circle())

            #lets the computer give specific moves to respond to a specific condition in the gameboard
            
            r = 0   # not need to give row as the disc will drop into the last available space
            c = 6   # the 6th (starting from 1 = 7th) column
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()    
        
    def ai_1 (self):
        is_space_free = False  
        
        if (is_space_free == False):
            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 5
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()    

        
    def ai_2 (self):
        is_space_free = False   
        
        if (is_space_free == False): 
            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 4
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()    
        
    def ai_3 (self):
        is_space_free = False  
        
        if (is_space_free == False): 

            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 3
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()    
        
    def ai_4 (self):
        is_space_free = False   #assign is_space_free as a False (not) value
        
        if (is_space_free == False): 

            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 2
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()
        
    def ai_5 (self):
        is_space_free = False   
        
        if (is_space_free == False): 
            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 1
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()

    def ai_6 (self):
        is_space_free = False   
        
        if (is_space_free == False): 

            print ("Player %s turn" %self.get_player_circle())
            r = 0
            c = 0
            self.button = self.buttons_2d_list[r][c]
            is_space_free = self.button["text"] == " "

            
        self.button.invoke()
        
        
        

        
    def play_small(self): #this method is used for the small connect 4 grid 
                
        is_space_free = False   

        while (is_space_free == False): 

            
            print ("Player %s turn" %self.get_player_circle())  
            
        
            r = random.randint (0,5-2)   #take 2 away from the starndard move used in the 7x6 grid
                                        
            c = random.randint (0,6-2)

            self.button = self.buttons_2d_list[r][c]    
            
            is_space_free = self.button["text"] == " "
            
            
        self.button.invoke()    

    def play_large(self):   # method for larger grid size
                
        is_space_free = False   

        while (is_space_free == False):

            
            print ("Player %s turn" %self.get_player_circle())  
            
        
            r = random.randint (0,5+2)    #addtion of 2 from the standard size
                                        
            c = random.randint (0,6+2)

            self.button = self.buttons_2d_list[r][c]    
            
            is_space_free = self.button["text"] == " "  
            
        self.button.invoke()   


