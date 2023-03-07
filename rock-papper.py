import random 


def play():
    user = input("r->rock, p->paper, s->scissors\t")
    computer = random.choice(['r','p','s'])
    print(computer)

    if user == computer:
        return 'tie'
    if  is_win(user,computer):
        return 'You Won!'
    
    return 'You Lost'

def is_win(player, oppenent):
    
    if (player == 'r' and oppenent == 's')  or (player =='s' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
        return True
    
print(play())