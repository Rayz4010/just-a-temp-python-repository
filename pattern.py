'''
Pattern Printing
Print a triangle pattern:
*
**
***
****
*****
taking n=5
use n as user input'''

'''psudocode:
defining a function to call the pattern
    use a for loop to make the code iterate 
    print the pattern
    the function wont return any value
taking n as user input
call the function
'''

# defining the function
def pat(n):
    # using the for loop to iterate 
    for x in range (1,n+1):
        #printing x
        print('*'*x)

#taking the user input
num=int(input("Enter how long the pattern will be:"))

#calling the func 
pat(num)


