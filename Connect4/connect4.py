# This is the main menu for the connect 4 game which is text based
# Importing all classes from files 
from gui import GameGUI
from tkinter import messagebox
from sys import exit    #used to exit the game
from gameboard import GameBoard
from sim import Simulator
from gui import Grid_mode
from gui import Difficulty_GameGUI
from subprocess import call #used for changing colour in method below


def plays():    # the play method which is is called by the game_menu
        
        b_gui = GameGUI()               # assign the class of the standard Connect 4 game GUI to variable b_gui (creates new instance of class)  
        b_gui.intialise_dynamic()       # creating a method reference to the creation of the Connect 4 Grid GUI
        gui = b_gui                     # assigning the variable to the file


def difficulty():       # this method called by the modes_menu method calls the class which has multiple AI difficulties 
           b_gui = Difficulty_GameGUI()
           b_gui.intialise_dynamic()
           gui = b_gui

                               
    
def pause():            # pause method called after every game and displays text in python shell, and also acts as a pause
    print("\nCONNECT 4")
    input("\nPress Enter Key to Resume:")       #requires user to press a key to return to continue
    

    
            
    
def modes_menu():       # a sencondary menu which branches from the game_menu, lets users access adittional game modes
    while True:         # while loop, excecutes constantly until exited/false
        print ("")
        print("NEW MODES")
        print("a - Grid Size")
        print("b - Difficulty")
        print("c - Return to Menu")     #display a list of options to the user
        
        option = input("Your option: ") #assigning keyboard input (character) to the varibale (option)
        option = option.lower()         #the character will change to lower case if not already
        print(" ")
        if option == "a":               #if loop, if True only once, exceute the method
                grid_size()
        elif option == "b":             #elif loop, else (exceuted when previous if statement is false), if elif statement is true it will exceute method
                difficulty()
        elif option == "c":
                game_menu()
        else:
                print("Invalid menu option (a,b,c)")    #displayed if user enters incrorrect value/character
                print("Try Again!!!")
                modes_menu()                            #the modes_menu is called immediatley after user enters incorrect option               
                

def grid_size():        #user can select size of connect 4 grid
        while True:
                print("\t1 = SMALL(5x4)\t 2 = Default(7x6)\t3 = Large(9x8)\n")
                print ("\t4 = Return to Mode Menu\n")
                try:            #try/except statement, prevents from python displaying error when excecuted
                        g =int(input("Enter the number of the grid you wish to play with: "))
                        print(" ")
                        if g == 1:                      #small connect 4 GUI grid  
                                g_gui = Grid_mode()     
                                g_gui.small_grid()
                                gui = g_gui
                                pause()
                                main()
                        elif g == 2:                    # standard 7x6 connect 4 GUI grid
                                b_gui = GameGUI()
                                b_gui.intialise_dynamic()
                                gui = b_gui
                                pause()
                                main()
                        elif g == 3:                    # large connect 4 GUI grid
                                g_gui = Grid_mode()
                                g_gui.large_grid()
                                gui = g_gui
                                pause()
                                main()
                        elif g == 4:
                                modes_menu()            #retruns to modes_menu
                                
                        else:
                                print("")
                                print("invalid menu option")
                                grid_size()
                except ValueError:                      # if user enters a value/number the print statement displayed
                    print("\nTry Again!!!")
                        
        


        
def game_menu():        #the main screen that the user will see
    while True:
        call('color a', shell=True)     #changes colour of text in command line interface NOT IDLE, uses the call import.
                                        #colour changes to green
        print ("\n\t\t\t\t  CONNECT 4 (2016)")
        print("\t\t\t\t  =================")
        print("\t\t\t\t 1 - Play: PVP - Play vs. AI (7x6) ")
        print("\t\t\t\t 2 - Simulation (AI vs. AI)(7x6)")
        print("\t\t\t\t 3 - New Modes (Grid size, Difficulty) ")
        print("\t\t\t\t 4 - Save/Load Game")
        print("\t\t\t\t 5 - Rules ")
        print("\t\t\t\t 6 - Quit ")
        try:
            option = int(input("\t\t\t\t Your option: "))
            print(" ")
            if option == 1:
                plays()
                print ("")
                print("\n\t\t\t\tGood Game!!!")
                pause()
                main()
            elif option == 2:
                simulator()
            elif option == 3:
                modes_menu()
            elif option == 4:
                load_board()    #The game is saved as a list in a text file, however the load function does not work
            elif option == 5:
                rules ()
            elif option == 6:
                quit()
            else:
                print("\t\tInvalid menu option")
                
        except ValueError:
            print("Try Again!!!")


def simulator():        #refrences the simulator class where the AI play against eachother
        s_gui = Simulator()        
        s_gui.intialise_dynamic()
        sim = s_gui

        
def load_board():       #refrences the GUI of connect 4, however it also refereces the loading method. This is to load the game into the GUI.
        b_gui = GameGUI()
        b_gui.load = True;
        b_gui.intialise_dynamic()
        gui = b_gui
        

def rules ():           #rules of the connect 4 game
        print("\t\t\t\tCONNECT 4 RULES\n")
        print("\t\t\t1. Select the game mode from the menu\n")
        print("\t\t\t2. Select the colour of your disc\n")
        print("\t\t\t3. Place the disc in the empty space in the grid\n")
        print("\t\t\t4. Connect 4 discs of the same colour to win\n")
        print("\t\t\t5. Have a good game!!!\n\n")


        input("\t\t\tPress any button to retrun to the main menu >\n ")

        
def main():     #main method has the highest priority, this holds the start method.
    game_menu() 
main()
