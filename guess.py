'''
Guess the Number
Create a simple number-guessing game where the user has to guess a randomly generated number between 1 and 100. 
Give hints like "Too High" or "Too Low" until the correct number is guessed.
'''

'''
Psudocode:
first import random
then make a variable that stores the random number
then make a function to guess the number 
    then make a while loop to keep the game running,pass the number x into the function
    take a input from the user
    if the input is equal to the number then print bingo and break the loop
    or just print too high or too low
It wont return any value
'''

#stating the code by importing random
import random

#making the function
def game(num):
    x=num #just making it most easier to find you can ignore it
    #putting in a infinite state so it continues till the game ends
    while True:
        #making the input itearative for the prompt
        inp=int(input("Enter your guess: "))
        #checking the input is output
        if inp==x:
            print ("Bingo!Thats the correct answer")
            break
        #higher case
        elif inp>x:
            print ("Wrong! the number you've entered is higher than the answer")
        #lower case
        elif inp<x:
            print ("Wrong! the number you've entered is lower than the answer")
        #taking the default case
        elif inp<0:
            print ("Please enter a valid number")

    
#taking a variable to store thr random number between 1-100
final_num=random.randint(0,101)
#testing random and its working
#calling the function
print ("Are you ready to take a guess of the number between 1-100 \nLETS START")
print ("But before starting you need to know one rule \n***1.You need to only input whole numbers***\n***2.You can guess infinite number of times***")
game(final_num)

'''
This concludes the program
'''
