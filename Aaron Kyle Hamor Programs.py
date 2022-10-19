#Everything within this file, except for maybe some comments, was not made by me
#The functions within this file were made by Aaron Kyle Hamor.

#====================================#

#Imports#

from random import choices, randint, shuffle

#====================================#

#Chapter 7 Python Exercise 12, 2022

#===#

#white_elephant takes no arguments
#white elepahnt takes groups of people and pairs them up
#people in the same group can not be paired together
#outputs list of pairs
def white_elephant1():
    #group people together
    dev_dept = ["Julia", "Oliver", "Abigail"]
    hr_dept = ["Camden", "Kayleigh", "Cooper", "Kerrigan"]
    sales_dept = ["Avery", "Charlotte", "Elle"]
    shuffle(dev_dept)
    shuffle(hr_dept)
    shuffle(sales_dept)
    #create list of matches
    match_list = []
    #put values in dev dept
    for value in dev_dept:
        match_list.append(value)
    #put values in every other space in match list
    for index, value in enumerate(hr_dept):
        match_list.insert(index * 2, value)
    #put values in every other space in match list
    for index, value in enumerate(sales_dept):
        match_list.insert(index * 2, value)
    #output results
    print("Here are the results")
    for index, person in enumerate(match_list):
        print(f"{person} gifts to {match_list[index-1]}")
        
#====================================#
        
#Chapter 7 Python Exercise 11, 2022
        
#===#
        
#tic_tac_toe takes no arguments
#creates a randomly played tic tac toe game
#returns gameboard and winner
def tic_tac_toe():
    #initialize blank board
    game_board = [["-","-","-"],["-", "-", "-"],["-", "-", "-"]]
    winner = None
    #set starting player to X (0=X, 1=0)
    player = 0
    #loops once for every space on board unless someone wins
    for index in range(9):
        #value_board is game_board filtered to x values with a "-"
        #filters game_board and creates a tuple with the list at x location
        #and the index of that list in the origional board
        value_board = [(index, x) for index, x in enumerate(game_board) if "-" in x]
        #chooses a random x value from the length of value board
        #x_val used only for value_board!!!
        x_val = randint(0, len(value_board) -1)
        #creates a list of the indexes of all the "-" values
        y_list = [index for index, x in enumerate(value_board[x_val][1]) if x is "-"]
        #chooses a random y_val from y_list
        y_val = choices(y_list, k=1)[0]
        #gets corresponding x val in game_board
        x_val = value_board[x_val][0]
        #checks if player = X
        if not player:
            game_board[x_val][y_val] = "X"
            player = 1
        #player = 0
        else:
            game_board[x_val][y_val] = "0"
            player = 0
        #checks for game winner after 4 turns have passed
        if index > 3:
            #calls gameover to test for winner, returns T/F
            is_over = gameover(game_board, [x_val, y_val])
            if is_over:
                #gets player at final played location
                winner = game_board[x_val][y_val]
                break
    #display board        
    for row in game_board:
        print(row)
    #checks if a winner exists and outputs message accordingly
    if not winner:
        print("The game was a tie.")
    else:
        print(f"{winner} won the game.")

#gameover takes two arguments (game board, (x, y) pos of last move)
#checks if a player has won tic tac toe
#reutrns true if a player has won, else returns false
def gameover(board, pos):
    x = pos[0]
    y = pos[1]
    #test horizontal
    if board[0][y] == board[1][y] == board[2][y] != "-":
        return True
    #test vertical
    if board[x][0] == board[x][1] == board[x][2] != "-":
        return True
    #test diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    #no win statements are true
    return False

#====================================#
        
#Chapter 7 Python Exercise 3, 2022
        
#===#

#rainfall takes no inputs
#asks for rainfall of each month
#returns the min and max months and total and average
def rainfall():
    #list of months
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfall_list = []
    for month in months:
        #try to convert input to int
        try:
            rainfall = int(input(f"Enter the rainfall for {month}: "))
            #input validation
            while rainfall < 0:
                print("Rainfall must be positive.")
                rainfall = int(input(f"Enter the rainfall for {month}: "))
            #populate list
            rainfall_list.append(rainfall)
        #can't convert to int error
        except ValueError:
            print("Invalid value. Exiting...")
            return
        #general exception error
        except Exception:
            print("Something went wrong. Exiting...")
            return 
    #month with least value and index        
    least_month_index = rainfall_list.index(min(rainfall_list))
    least_month = months[least_month_index]
    #month with greatest value and index 
    max_month_index = rainfall_list.index(max(rainfall_list))
    max_month = months[max_month_index]
    #output statements
    print(f"{least_month} had the least rain with {rainfall_list[least_month_index]} inches of rain.")
    print(f"{max_month} had the most rain with {rainfall_list[max_month_index]} inches of rain.")
    print(f"Total rain for the year: {sum(rainfall_list)}")
    print(f"Average rain per month: {sum(rainfall_list)/12}")
    
#====================================#
        
#Chapter 7 Python Exercise 7, 2022
        
#===#
    
#drivers_exam takes no arguments
#scores a drivers exam test file
#returns the amount of missed questions and if user passed
def drivers_exam():
    #creates a possibly infinate loop
    while True:
        #get name of the file
        test_name = input("Please enter the name of the file to read: ")
        #try to open the files
        try:
            #opens the users file saving lines in list
            with open(test_name, "r") as file:
                tester_answers = [answer.rstrip("\n") for answer in file]
            #opens the key file saving lines in list
            with open("driver_test_key.txt", "r") as key:
                key_answers = [answer.rstrip("\n") for answer in key]
            #checks answer total = key answer total
            if not len(tester_answers) == len(key_answers):
                print("The amount of answers in the file do not match that of the key.")
                continue
            score = len(key_answers)
            wrong_answers = []
            #loop through answers, if wrong save problem # and decrease score
            for index, answer in enumerate(tester_answers):
                if not answer == key_answers[index]:
                    wrong_answers.append(index + 1)
                    score -= 1
            #primary output statements
            print("\nTest Grading Complete\n")
            print(f"You answered {score} correctly out of {len(key_answers)}")
            print(f"You missed {len(wrong_answers)} questions. The minimum you could miss to pass is 5.")
            #checks if user missed questions
            if not len(wrong_answers) == 0:
                #checks if user passed the exam
                if len(wrong_answers) > 5:
                    print("You failed the exam. Study and try again.")
                else:
                    print("You passed!")
                print(f"Here are the questions you missed \n{wrong_answers}\n")
            #perfect score
            else:
                print("You passed!")
        #file was not found error    
        except FileNotFoundError:
            print("There was an error opening a file.")
        #error reading the file
        except IOError:
            print("Error reading a file.")
        #general exception error
        except Exception as err:
            print("There was an error." + str(err))
        #promts user to check another test and continue loop    
        cont = input("Check another test? (y/n): ")
        if cont == "n":
            break