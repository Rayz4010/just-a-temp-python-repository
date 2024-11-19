'''
Count Vowels
Write a program to count the number of vowels in a given string.
'''

'''This program is used to count the number of vowels inside the string 
so lets start with the program'''



#taking the input
def check(s): 
    # declearing a variable for list and vowel
    x=[]
    v=['a','e','i','o','u']
    for t in v:
        #checking if the vowel is present in the string
        if t in s:
            #listing it into the list
            x.append(t)
    #returtning the list
    return x


#input from the user
string=input("Enter the string to count the number of vowels: ")
#call the function    
y=check(string)

print(y)

''' this concludes  the program and the logic'''