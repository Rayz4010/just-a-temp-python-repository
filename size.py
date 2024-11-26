'''
Find Maximum and Minimum
Write a program to find the maximum and minimum numbers in a list.
'''

'''
Psudocode:
Take a list
the make a function to find the largest
    using math module max to return the largest valur
the make a function to find the smallest
    using min to return the minimum value
 '''

#starting the code 
def maxi(l):
    mmax=max(l)
    return mmax

def mini(l):
      mmin=min(l)
      return mmin
        

lim=int(input("Enter the limit of the list :"))
up=0 #updation variable 
list=[] #the list
while up<lim:
    put=int(input("Enter the list values :"))#taking a value to append  in the list
    #appending the list
    list.append(put)
    up=up+1

#print the list
print("The list you entered is: ")
print(list)
#calling the functions
maxima=maxi(list)
minima=mini(list)
print("The largest value in the list is: ",maxima)
print("The smallest value in the list is: ",minima)


'''This concludes the program even though ive used the build in module 
idk if its fair or not'''




