#SLOT MACHINE
import random
random_things=["7","BAR"]
start=True
fruits=[[],
        [],
        []]
for i in range(3):
    for j in range(3):
        fruits[i].append(random.choice(random_things))

def lucky(fruits):
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
    if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == 'BAR') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == 'BAR') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == 'BAR')):
        if random.randint(0,100) <= 50:
             multiplier=2
        else:
            multiplier=1
    if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == '7') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == '7') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == '7')):
        if random.randint(0,100) <= 10:
            multiplier=3
        else:
            multiplier=1
    return multiplier

def actual_programm(user_deposit,winner,mult,fruits):
    while start==True:
        global c
        global user_money
        global game_earned
        user_money=0
        game_earned=0
        spin=5
        restart=True
        c=0
        winning_line=[]
        if fruits[0][0] == fruits[0][1] == fruits[0][2]: 
            winning_line.append(1)
        if fruits[1][0] == fruits[1][1] == fruits[1][2]:
            winning_line.append(2)
        if fruits[2][0] == fruits[2][1] == fruits[2][2]:
            winning_line.append(3)
        multiplier = 1
        if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == 'BAR') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == 'BAR') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == 'BAR')):
            if random.randint(0,100) <= 50:
                 multiplier=2
            else:
                multiplier=1
        if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == '7') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == '7') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == '7')):
            if random.randint(0,100) <= 10:
                multiplier=3
            else:
                multiplier=1
        while user_deposit >= 5 and restart == True:
            
            game_earned+=user_deposit
            
            bet_line=input("Give me the line that you want to bet(1-3): ")
            print "============================="
            while bet_line != 1 and bet_line != 2 and bet_line != 3:
                print "Inccorect Line"
                print "=============="
                bet_line=input("Give me the line that you want to bet(1-3): ")
                print "============================="
            if c != 0:
                for i in range(3):
                    for j in range(3):
                        fruits[i].append(random.choice(random_things))
                winning_line=[]
            if fruits[0][0] == fruits[0][1] == fruits[0][2]:
                winning_line.append(1)
            if fruits[1][0] == fruits[1][1] == fruits[1][2]:
                winning_line.append(2)
            if fruits[2][0] == fruits[2][1] == fruits[2][2]:
                winning_line.append(3)
                multiplier = 1
            if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == 'BAR') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == 'BAR') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == 'BAR')):
                if random.randint(0,100) <= 50:
                    multiplier=2
                else:
                    multiplier=1
            if ((fruits[0][0] == fruits[0][1] == fruits[0][2] and fruits[0][0] == fruits[0][1] == fruits[0][2] == '7') or (fruits[1][0] == fruits[1][1] == fruits[1][2] and fruits[1][0] == fruits[1][1] == fruits[1][2] == '7') or (fruits[2][0] == fruits[2][1] == fruits[2][2] and fruits[2][0] == fruits[2][1] == fruits[2][2] == '7')):
                if random.randint(0,100) <= 10:
                    multiplier=3
                else:
                    multiplier=1
            c+=1
            if winning_line == []:
                print"No winners this round"
                print "======================"
            if bet_line in winning_line:
                money_won=(1.2*user_deposit)*multiplier
                print "You won",money_won
                print "============"
                user_money=user_money+money_won+user_deposit
                game_earned-=money_won
            else:
                print "Sadly you lost your money"
                print "=============="
                user_money-=user_deposit
            
            if user_money > 0:
                print "You're up",user_money,"$"
                print "============"
            else:
                print "You're down",abs(user_money),"$"
                print "==========="
            for i in range(len(fruits)):
                    print fruits[i]
            
            playagain=raw_input("do you want to play again (Y/N): ")
            while playagain != "Y" and playagain != "N":
                print "Wrong Answer"
                playagain=raw_input("do you want to play again (Y/N): ")
            if playagain == 'Y':
                restart == True
                user_deposit=input("Give the amount of money that you want to bet: ")
                if user_deposit < 5:
                    print "Sadly you have to add more than 5$ to play"
                    print "=========================================="
                    return "Thanks for playing"
            
                fruits=[[],
                        [],
                        []]                      
            else:
                restart == False
                return "Thanks for playing"


while start == True:        
    print "           RULES"
    print"============================="
    print "YOU HAVE TO PUT > 5 $ TO PLAY"
    print "============================="
    print "if you win + bet line is all 7's you have 1 in 10 chances to have a 3x multiplier"
    print "============================="
    print "if you win + bet line is all BAR you have 5 in 10 chances for a 2x multiplier"
    print "============================="
    print "The amount you bet if you win gets multiplied *1.2+ the deposit amount"
    print "============================="
    print "IF YOU LOSE ALL YOUR MONEY GETS LOST"
    print "============================="
    user_deposit=input("Give the amount of money that you want to bet: ")
    if user_deposit < 5:
        print "Not enough money for a spin"
    else:
        winner=lucky(fruits)
        mult=money_earned(fruits)
        runner=actual_programm(user_deposit,winner,mult,fruits)
        print runner
        print "==============="
        if user_money >= 0:
            print "Total money you made",user_money,"$"
            print "==================="
        else:
            print "You lost",abs(user_money),"$"
            print "=================="
        admin_pass_given=raw_input("Press any key to continue... ")
        admin_pass=open("password.txt","r")
        admin_pass=admin_pass.read()
        if admin_pass_given == admin_pass:
            if game_earned >= 0:
                print "Total money made by the casino",game_earned,"$"
            else:
                print "Total money lost by the casino",abs(game_earned),"$"
            finish_game=raw_input("Do you want to finish the game?(Y/N) ")
            while finish_game not in ["Y","N"]:
                finish_game=raw_input("Do you want to finish the game?(Y/N) ")
            if finish_game == "Y":
                start=False
        

