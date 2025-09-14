#!/usr/bin/env python
# coding: utf-8

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
# (using input), compare them, print out a message of congratulations to the
# winner, and ask if the players want to start a new game)
# Remember the rules:
#  Rock beats scissors
#  Scissors beats paper
#  Paper beats rock

# In[ ]:


player1 = input('player 1, enter Rock, Paper, or Scissors').lower()
player2 = input('player 2, enter Rock, Paper, or Scissors').lower()

if player1 == player2:
     print('its a draw!')

elif(
    (player1 == 'scissors' and player2 == 'rock') or
     (player1 == 'rock' and player2 == 'paper') or
     (player1 == 'paper' and player2 == 'scissors')
    ):
     print("congratulations player1 ! You've won!")

    
elif(
    (player2 == 'paper' and player1 == 'rock') or
    (player2 == 'rock' and player1 == 'scissors') or
    (player2 == 'scissors' and player1 == 'paper') 
) :
    print("congratulations player2 ! You've won!")

else:
    print( 'not applicable, enter rock scissors or paper to continue')

again= input('Do you want to play again ? yayy/naa').lower()
if again == yayy :
    print('welcome back')
elif again == Naa:
    print('Bye!. Thanks for playing')

 


# In[ ]:




