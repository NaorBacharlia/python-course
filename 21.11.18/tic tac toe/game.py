game_play = [[0 for i in range(3)] for i in range(3)]
X_wins = 0
O_wins = 0
draw = 0
turn_num = 0
def print_play_game():
    print()
    for i in range(3):
        print("-------------")
        print("| {} | {} | {} |".format(game_play[i][0],game_play[i][1],game_play[i][2]))
    print("-------------")
        
        

# game initialization
def inintialize_game():
    global turn_num 
    turn_num = 0
    a =1
    for i in range(3):
        for j in range(3):
            game_play[i][j] = a
            a+=1
# check that the place is free
def is_valid_choice(choice):
    
    for i in range(3):
        for j in range(3):
            if game_play[i][j] == int(choice):
                return True
    return False # the place is occupied

#get player choice and check if the choice is valid
def get_player_choice(player_turn):

    player_choice = input("Player with {} enter your number:".format(player_turn))
    if not player_choice.isdigit():
        print("Please enter valid number (1-9)")
    elif int(player_choice) >9 or int(player_choice) <=0:
        print("Please enter valid number (1-9)")
    elif not is_valid_choice(player_choice):
        print("this place is occupied, try again")
    else:
        return int(player_choice)
    return get_player_choice(player_turn)
# add the player choice to location in the matrix game
def set_player_choice(player_choice, player_turn):

    for i in range(3):
        for j in range(3):
            if game_play[i][j] == player_choice:
                game_play[i][j] = player_turn
                break
# check for each row if there is a winner
def row_check():
    for i in range(3):
        x=0
        temp = game_play[i][0]
        for j in range(3):
            if temp == game_play[i][j]:
                x+=1
        if x == 3:
            return game_play[i][j]
    return ""
# check for each col if there is a winner      
def col_check():
    for i in range(3):
        x=0
        temp = game_play[0][i]
        for j in range(3):
            if temp == game_play[j][i]:
                x+=1
        if x == 3:
            return game_play[j][i]
    return ""
            
# check all the options for winner
def is_winner():
    # col check
    col = col_check()
    row = row_check()
    if col != "":
        print("col")
        return col
    elif row != "":
        print("row")
        return row
   
    #  main diagonal check
    topLeft = game_play[0][0]
    center = game_play[1][1]
    bottomRight = game_play[2][2]
    if bottomRight == center and center == topLeft:
        return center
    # second diagonal check
    topRight = game_play[0][2]
    bottomLeft = game_play[2][0]
    if topRight == center and center == bottomLeft:
        return center
    return ""
                    
def ask_do_you_want_to_continue():
    x = input("do you want to continue(Y/N)")
    if x.lower() == "y":
        inintialize_game()
        print_play_game()
        game()

    elif x.lower() == "n":
        return False
    else:
        input("enter valid choice do you want to continue(Y/N)")
        ask_do_you_want_to_continue()

def game():
    global X_wins
    global O_wins
    global draw
    global turn_num 
    is_game_on = True
    turn_num =0
    print_play_game()
   
    player_choice = ""
    
    player_turn = ""
    while is_game_on:
        print("round Number: {} ".format(turn_num))
        # check who's playing
        if turn_num % 2 ==0:
            player_turn = "X"
        else:
            player_turn = "O"
        # get and check for valid player choice
        player_choice = get_player_choice(player_turn)
        # save the player choice in the game board
        set_player_choice(player_choice, player_turn)
        # print the game board 
        print_play_game()
        
        # check if there is winner just after 6 turns
        if turn_num >=4:
            
            winner = is_winner()
            if winner == "X":
                X_wins += 1
                print("The winner is player X")
                print("num of X win is {}".format(X_wins))
                print("num of O win is {}".format(O_wins))
                is_game_on = ask_do_you_want_to_continue()
               
            elif winner == "O":
                O_wins += 1
                print("The winner is player O")
                print("num of O win is {}".format(O_wins))
                print("num of X win is {}".format(X_wins))
                is_game_on = ask_do_you_want_to_continue()
                
        turn_num += 1
        if turn_num > 8:
            draw += 1
            print("There is no winner, num of draws {}".format(draw))
            print("num of O win is {}".format(O_wins))
            print("num of X win is {}".format(X_wins))
            is_game_on = ask_do_you_want_to_continue()
        
        
                
        

inintialize_game() # set the board for the game
# start the game
game()
print("thank you for play with us")   
            





