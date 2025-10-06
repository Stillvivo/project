import random
print("rock...")
print("paper...")
print("scissors...")
print(".............................")
 
Randomnumber = random.randint(0, 2)
Computermove = ""

if Randomnumber == 0:
    Computermove = "paper"
elif Randomnumber == 1:
    Computermove = "rock"
elif Randomnumber == 2:
   Computermove = "scissors"

player1_wins = 0
player2_wins = 0
winning_score = 4

while player1_wins < winning_score and player2_wins < winning_score:
    print(f"player 1  : {player1_wins} and player 2  : {player2_wins}")
    player_1 = input("player_1 make your move :")
    print(f"player_2 , make your move : {Computermove}")
    player_2 = Computermove

    if player_1 == "q" or player_1 == "quit":
        break

    if player_1 == "paper":
        if player_2 == "rock":
            print("player_1 winner!!!")
            player1_wins =+ 1
        elif player_2  == "scissors": 
            print("player_2 winner!!!")
            player2_wins += 1

    if player_1 == "scissors":
        if player_2 == "rock":
            print("player_2 winner..!")
            player2_wins += 1
        elif player_2 == "paper":
            print("player_1 winner...!")
            player1_wins =+ 1


    if player_1 == "rock":
        if player_2 == "scissors":
            print("player_1 winner!...")
            player1_wins =+ 1
        elif player_2 == "paper":
            print("player_2 winner!...")
            player2_wins += 1


    if player_1 == player_2:
     print("thats tie")
        
print(f" final scores : player 1  : {player1_wins} | player 2  : {player2_wins}")
