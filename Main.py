#welcome the players

print('welcome!')
print('This is Rock, Paper and Scissors')
print('The game should be played by two players')
print('The rules for this game are Paper covers Rock,Rock beats Scisssors,Scissors cuts Paper ')
print('Enter choice\n R for Rock, \n S for Scissors and \n P for Paper\n')

import random

while True:

    choices = ('R','P','S')
    computer = random.choice(choices)
    print('computer: ',computer)

#take the input from player
    player= input('player enter the choice: ')
    possible_actions = ('R','P','S')

    if computer == player:
        print(f'The choices are the same. It is a tie!')

    elif computer == 'R':
      if player == 'S':
        print('Rock beats Scissors! You win!')
    
    else:
        print('Paper covers Rock! You lose!')

    if computer =='P':
      if player =='R':
        print('Paper covers Rock, You win!')
    else:
        print('Scissors cuts Paper, You lose!')
    
    if computer== 'S':
      if player == 'P':
        print('Scissors cuts Paper, You win!')
    else:
        print('Rock beats Scissors, You lose!')

    continue_game = input('would you like to continue?(Yes\ no): ').lower

    if continue_game != 'yes':
     break

print('bye')




