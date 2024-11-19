'''
Prime Number Check
Write a program to check if a number is a prime number.
'''

p=int(input("Enter the number to check if it is prime or not: "))


#defining the function
def func(n):
    #checking the number
    if n==1 or n==0:
        print("The number cant be 0 or 1")
    elif n==2 or n==3:
        print("The number",n,"is prime")
    #checking if its prime or not
    for i in range (2,n-1):
        if n%i==0:
            print("number",n," is not a prime")
            break
        else:
            print("the number",n,"is prime")
            break

#calling the function
func(p)

''' this concludes the program  with logic'''