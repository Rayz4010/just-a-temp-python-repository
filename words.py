'''
Count Words
Write a program that counts the number of words in a sentence.
'''

'''
Psudocode:
First we have to take make a string and input the sentence
Defining a function cause its cool
    just use the build in function
print the count
'''

#Lets start with the program
def count (string):
    #just using this inbuild function
    return len(string.split())

'''
Defining the main function now
'''
print("Counting the no of words in a sentence")
string=input("Enter the sentence: ") #taking the input from the user
count=count(string) #calling the function
print("The no of words in the sentence is: ",count) #printing the count

'''
This concludes the program

pretty accurate
'''