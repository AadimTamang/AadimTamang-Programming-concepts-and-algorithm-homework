player1 = input("Player 1, enter your choice (rock, paper, scissors): ")
player2 = input("Player 2, enter your choice (rock, paper, scissors): ")

if player1 == player2:
    result = "It's a tie!"
elif (player1 == 'rock' and player2 == 'scissors') or \
     (player1 == 'scissors' and player2 == 'paper') or \
     (player1 == 'paper' and player2 == 'rock'):
    result = "Player 1 wins!"
else:
    result = "Player 2 wins!"