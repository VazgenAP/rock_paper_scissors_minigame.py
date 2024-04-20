import random

choice = {'rock': 'r', 'paper': 'p', 'scissors': 's'}  # Working with dictionary
choice_keys = list(choice.values())

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(choice_keys)

    if user == computer:
        return "It's a tie"
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won'
    
    return 'You lost'

def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r  -> conditions of winning 
    if (player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
while True:  # Incorporate a 'while' loop to continue the game until the user achieves victory
    n = play()
    print(n)
    if n == 'You won':
        break
