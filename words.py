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
    string.strip() #removing the spaces from front and back
    #initasializing the count to 1 because the last wite space is stripped so there is no possible way to count the last word so just initalizing the count to 1 in the progarm only
    count=0 #count
    #the for loop
    for x in string:
        #checking if there is a white space update cout by 1
        if x==" " or string.endswith(".") or string.endswith(" "):
            count+=1 #updating the count by 1

    return count

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