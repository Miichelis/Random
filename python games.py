#PYTHON GAMES


print "Welcome To My Py Games"


type_of_game=input("For the Random Number Guesser type 1 and for the Quiz game type 2 ")


if type_of_game == 1:
    import random

    print "Welcome To The Random Number Guesser!"

    top_range=input("Give me up to what number you want to be able to guess: ")

    if top_range < 0:
        print "give me a number higher than 0"
        quit()


    random_number=random.randint(0,top_range)

    guesses=0

    while True:
          guesses+=1
          user_guess=input("Guess The Number ")
          if user_guess == random_number:
            
              print "You Got It!"
              break
          elif user_guess > random_number:
              print "You were above the number"
          else:
              print "You were below the number"

    if guesses == 1:
        print "Congrats You Got a Perfect Score!"
    else:
        print "You Got It In" , guesses, "Guesses"
       

elif type_of_game == 2:

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
   
else:
    quit()

   









