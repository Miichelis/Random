#PYTHON GAMES
import random

print "Welcome To My Py Games"
games=[1,2,3]
restart=["yes","no"]
type_of_game=input("For the Random Number Guesser type 1, for the Quiz game type 2 and for rock paper scissors type 3 ")
while type_of_game not in games:
    type_of_game=input("For the Random Number Guesser type 1, for the Quiz game type 2 and for rock paper scissors type 3 ")

def random_number_guesser():
    run=True
    while run == True:
        print "Welcome To The Random Number Guesser!"

        top_range=input("Give me up to what number you want to be able to guess: ")
        while top_range < 0:
            top_range=input("Give me up to what number you want to be able to guess: ")
        random_number=random.randint(0,top_range)
        guesses=1
        user_guess=input("Guess The Number ")
        if user_guess > random_number:
            print "You were above the number"
        elif user_guess < random_number:
            print "You were below the number"
        while user_guess != random_number:
              user_guess=input("Guess The Number ")
              guesses+=1
              if user_guess > random_number:
                  print "You were above the number"
              elif user_guess < random_number:
                  print "You were below the number"
        print "You Got It" 

        if guesses == 1:
            print "Congrats You Got a Perfect Score!"
        else:
            print "You Got It In" , guesses, "Guesses"
        playagain=raw_input("Wanna play again?('yes/no') ").lower()
        while playagain not in restart:
                print "Please type yes or no"
                playagain=raw_input("Wanna play again?('yes/no') ").lower()
        if playagain=="yes":
                    run=True
        elif playagain=="no":
                run=False
        print "Thanks for playing!"
           

def quiz():
    run=True
    while run == True:
        print "Welcome to my Quiz!"
        score = 0
        answer = raw_input("Question 1 ")
        if answer.lower() == "answer 1":
            
            print "Correct!"
            score += 1
        else:
            print "Incorrect!"
        answer2 = raw_input("Question 2 ")
        if answer2.lower() == "answer 2":
            print "Correct!"
            score += 1
        else:
            print  "Incorrect!"
        answer3 = raw_input("Question 3 ")
        if answer3.lower() == "answer 3":
             print "Correct!"
             score += 1
        else:
            print "Incorrect!"
        answer4 = raw_input("Question 4 ")
        if answer4.lower() == "answer 4":
            print "Correct!"
            score += 1
        else:
            print "Incorrect!"
        print "You Got" , score , "Out Of 4 Correct"
        print "Which Means You Got " , (score/4.0)*100.0 , "% Correct"
        playagain=raw_input("Wanna play again?('yes/no') ").lower()
        while playagain not in restart:
                print "Please type yes or no"
                playagain=raw_input("Wanna play again?('yes/no') ").lower()
        if playagain=="yes":
                run=True
        elif playagain=="no":
                run=False
        print "Thanks for playing!"

def rock_paper_scissors():
    run=True
    while run == True:
        cpu=["rock","paper","scissors"]
        choice_of_cpu=random.choice(cpu)

        player="nooptionselected"

        while player not in cpu:
            player=raw_input("Pick rock,paper,scissors: ").lower()


        print "Player:",player,"\n","Cpu:",choice_of_cpu


        if player=="rock" and choice_of_cpu=="paper":
            print "u lost"
        elif player=="paper" and choice_of_cpu=="rock":
            print "u won"
        elif player=="scissors" and choice_of_cpu=="paper":
            print "u won"
        elif player=="paper" and choice_of_cpu=="paper":
            print "tie"
        elif player=="scissors" and choice_of_cpu=="rock":
            print "u lost"
        elif player=="rock" and choice_of_cpu=="scissors":
            print "u won"
        elif player=="scissors" and choice_of_cpu=="scissors":
            print "tie"
        elif player=="rock" and choice_of_cpu=="rock":
            print "tie"
        elif player=="paper" and choice_of_cpu=="scissors":
            print "u lost"
        playagain=raw_input("Wanna play again?('yes/no') ").lower()
        while playagain not in restart:
            print "Please type yes or no"
            playagain=raw_input("Wanna play again?('yes/no') ").lower()
        if playagain=="yes":
            run=True
        if playagain=="no":
            run=False
        print "Thanks for playing!"



def gamesplay():
    if type_of_game==1:
        random_number_guesser()
    elif type_of_game==2:
        quiz()
    else:
        rock_paper_scissors()
gamesplay()
