'''
Count Words
Write a program that counts the number of words in a sentence.
'''

'''
Psudocode:
First we have to take make a string and input the sentence
Defining a function cause its cool
    stripping the front and back white spaces of the sentence
    now initialize count with 1 because the last word is not counted so just initializing the count to 1
    check if ' ' is present
        yes for count +1
        no for ignore
    return count
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