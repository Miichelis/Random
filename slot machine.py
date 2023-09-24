#deposit a sert am of money by the user
#bet on 3 lines of the slot machine
#run out of money = stop
#or cashout = stop
import random
random_things=["7","BAR"]

fruits=[[],
        [],
        []]



for i in range(3):
    for j in range(3):
        fruits[i].append(random.choice(random_things))
print fruits



def lucky():
    winning_line=[]
    if fruits[0][0] == fruits[0][1] == fruits[0][2]: 
        winning_line.append(1)
    if fruits[1][0] == fruits[1][1] == fruits[1][2]:
        winning_line.append(2)
    if fruits[2][0] == fruits[2][1] == fruits[2][2]:
        winning_line.append(3)
    return winning_line

def money_earned(fruits):
    multiplier = 1
    if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == '7') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == '7') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == '7')):
        multiplier = 3
    if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == 'BAR') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == 'BAR') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == 'BAR')):
        multiplier = 2
    
    return multiplier

    

def actual_programm(user_deposit,winner,mult,fruits):
    global c
    spin=5
    restart=True
    c=0
    while user_deposit >= 5 and restart == True:
        bet_line=input("Give me the line that you want to bet(1-3): ")
        if c != 0:
            for i in range(3):
                for j in range(3):
                    fruits[i].append(random.choice(random_things))
        c+=1
        if winner == []:
            print"No winners this round"
        if bet_line in winner:
            money_won=(1.2*user_deposit)*mult
            print "You won",money_won
            user_deposit+=money_won
        else:
            print "Sadly you lost"
       
        user_deposit-=spin
        print "Your balance is",user_deposit
        for i in range(len(fruits)):
                print fruits[i]
        
        playagain=raw_input("do you want to play again (Y/N): ")
        while playagain != "Y" and playagain != "N":
            print "Wrong Answer"
            playagain=raw_input("do you want to play again (Y/N): ")
        if playagain == 'Y':
            restart == True
            if user_deposit < 5:
                print "Sadly you have no money left"
                return "Thanks for playing"
            fruits=[[],
                    [],
                    []]
            winner=[]
                              
        else:
            restart == False
            return "Thanks for playing"
        

user_deposit=input("Give the amount of money that you want to bet: ")
if user_deposit < 5:
    print "Not enough money for a spin"
else:
    winner=lucky()
    mult=money_earned(fruits)
    runner=actual_programm(user_deposit,winner,mult,fruits)
    print runner
    print "Total money made =",c*5,"$"
        

