'''
Sum of Digits
Write a program to calculate the sum of digits of a number entered by the user.
'''

''' 
Okay i guess ive to use some iteration and define some function in this program
'''

#taking the input
num=int(input("Eneter the range of the number to be added"))


#defining the functin
def add(num):
    sum=0
    for i in range (0,num+1):
        sum=sum+i
    return sum


#calling the function
d=add(num)
print("The sum for the range of number",num,"is=",d)

'''this concudes the program with  logic'''

