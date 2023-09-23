#deposit a sert am of money by the user
#bet on 3 lines of the slot machine
#run out of money = stop
#or cashout = stop
import random
random_things=["7","BAR","dice"]

fruits=[[],
        [],
        []]



for i in range(3):
    for j in range(3):
        fruits[i].append(random.choice(random_things))



def lucky():
    if fruits[0][0] == fruits[0][1] == fruits[0][2]: 
        winning_line=1
    elif fruits[1][0] == fruits[1][1] == fruits[1][2]:
        winning_line=2
    elif fruits[2][0] == fruits[2][1] == fruits[2][2]:
        winning_line=3
    else:
        winning_line=0
    return winning_line

def money_earned(fruits):
    if ((fruits[0][0] == fruits[0][1] == fruits[0][2])or (fruits[1][0] == fruits[1][1] == fruits[1][2]) or (fruits[2][0] == fruits[2][1] == fruits[2][2])) == "7":
        multiplier = 5
    elif ((fruits[0][0] == fruits[0][1] == fruits[0][2])or (fruits[1][0] == fruits[1][1] == fruits[1][2]) or (fruits[2][0] == fruits[2][1] == fruits[2][2])) == "BAR":
        multiplier = 3
    else:
        multiplier = 1
    return multiplier

    

def actual_programm(user_deposit,winner,mult,fruits):
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
        if bet_line == winner:
            if winner != 0:
                win=(1.5*user_deposit)*mult
                print "You won",win
                user_deposit+=win
            else:
                print"No winners this round"
        else:
            print "Sadly you lost"
        
        user_deposit-=spin
        print "Your balance is",user_deposit
        for i in range(len(fruits)):
                print fruits[i]
        

        
        playagain=raw_input("do you want to play again (Y/N): ")
        while playagain != "Y" and playagain != "N":
            print "Wrong Answer"
            playagain=input("do you want to play again (Y/N): ")
        if playagain == 'Y':
            restart == True
            if user_deposit <= 5:
                print "Sadly you have no money left"
                print "Thanks for playing"
            fruits=[[],
                    [],
                    []]
                              
        else:
            restart == False
            print "Thanks for playing"
        

user_deposit=input("Give the amount of money that you want to bet: ")
if user_deposit < 5:
    print "Not enough money for a spin"
else:
    winner=lucky()
    mult=money_earned(fruits)
    runner=actual_programm(user_deposit,winner,mult,fruits)
    print runner
        

