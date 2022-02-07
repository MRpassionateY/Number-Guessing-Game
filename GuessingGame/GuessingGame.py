import random
number = int ( random.randint(1,10) )
lives = 2

print ( "  This is a number Guessing game. " )
guess = int ( input( "Guess a Number between 1 and 10 :- " ) )

while lives > 0 :
    if guess == number :
        print ( "Your Guess is Correct. You Win" )
        break;
    elif guess < number :
        print ( "Your Guess was wrong. The number is greater it." )
        guess = int ( input( "Guess a Number between 1 and 10 :- " ) )
        lives = lives - 1
    elif guess > number :
        print ( "Your Guess was wrong. The number is lesser it." )
        guess = int ( input( "Guess a Number between 1 and 10 :- " ) )
        lives = lives - 1

if lives == 0 :
    print ( "You Lost all your Lives." , "The number was" , number )