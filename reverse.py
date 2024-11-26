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


n = int(input("Enter the length of the list:"))
#taking the list
i=0
list=[]
while i<n:
    k=input("Enter the list:")
    list.append(k)
    i=i+1
rev(list)
