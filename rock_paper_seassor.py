#Importing nessasary file to hide user input 
import getpass
from getpass import getpass as input

#Printing the starting lines
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
# initilizing the score 
player1_score = 0
player2_score = 0
 
# Looping the game until one user wins 
while True: 
  player1Move = input("Player 1 Turn > ")
  print()
  player2Move = input("Player 2  Turn > ")
  print()

  if(player1Move=="R" or "r"):
    if(player2Move=="R" or "r"):
      print("draw!")

    elif(player2Move=="S" or "s"):
      print("Player1 Win")
      player1_score += 1

    elif(player2Move=="P" or "p"):
      print(" Player2 win")
      player2_score += 1

  elif(player1Move=="P" or "p"):

    if(player2Move=="R" or "r"):
      print("Player1 Win")
      player1_score += 1

    elif(player2Move=="S" or "s"):
      print("Player2 Win")
      player2_score += 1

    elif(player2Move=="P" or "p"):
      print(" Draw.")

  elif(player1Move=="S" or "s"):

    if(player2Move=="R" or "r"):
      print("Player 2 Win ")
      player2_score += 1

    elif(player2Move=="S" or "s"):
      print("Draw.")

    elif(player2Move=="P" or "p"):
      print("Player1 Win")
      player1_score += 1
    
#printing the wining scores for both

  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

# exiting on 3 win for either player
  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue
  
  # NOTE: if the code is not exiting after 3 wins, it's because the game is not being reset after each round
  # and also add a line to ask the players if they want to play again after each round
  # like this:
#   play_again = input("Do you want to play again? (yes/no): ")
#   if play_again.lower() != "yes":
#     break
#   else :
#     continue
  