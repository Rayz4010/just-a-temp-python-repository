'''
Reverse a List
Write a program to reverse a list without using built-in methods.
'''

''' Psudocode:
Its easy
first take a list
define a function
    no print it 
end lol
'''

'''im not sure if its the quesition same
lets start with it'''

#defining a function
def rev(l):
    print(l[::-1])

#defining the variables
i=0
list=[]

#taking the list length
n = int(input("Enter the length of the list:"))


#taking the list
while i<n:
    #taking a variable k to later join in the list since list takes ' ' as input
    k=input("Enter the list:")
    #pushing into the list
    list.append(k)
    #updating
    i=i+1

#calling the function
rev(list)


'''

This concludes the program
This one was a trickier one as the question was not clear


'''
