import random
'''
FUNCTIONS
'''

#for printing board
def print_board():
    print()
    print(x)
    print(y)
    print(z)
    print()

#human input
def checkh(ing):
    if ing<=8:
        if ing in c:
            print("Already filled")
            ing=int(input("Enter the position between 0-8: "))
            checkh(ing)
        else:
            c.append(ing)
    else:
        print("Invalid input")
def inputh(x,y,z):
    inh=int(input("Enter the position between 0-8: "))
    print(inh,type(inh))
    checkh(inh)
    #if inh>0 and inh<=2:
    if inh==0:
        x[0]="X"
    if inh==1:
        x[1]='X'
    if inh==3:
        x[2]='X'
    #if inh>3 and inh<=5:
    if inh==3:
        y[0]="X"
    if inh==4:
        y[1]='X'
    if inh==5:
            y[2]='X'
    #if inh>6 and inh<=8:
    if inh==6:
        z[0]="X"
    if inh==7:
        z[1]='X'
    if inh==8:
        z[2]='X'
    return x,y,z
    
#computer input
def checkc(inp):
    if inp in c:
        inp=random.randint(0,8)
        check(inp)
    else:
        c.append(inp)
def inputc(x,y,z):
    inp=random.randint(0,8)
    checkc(inp)
    if inp==0:
        x[0]="0"
    if inp==1:
        x[1]='0'
    if inp==3:
        x[2]='0'
    #if inp>3 and inh<=5:
    if inp==3:
        y[0]="0"
    if inp==4:
        y[1]='0'
    if inp==5:
        y[2]='0'
    #if inp>6 and inh<=8:
    if inp==6:
        z[0]="0"
    if inp==7:
        z[1]='0'
    if inp==8:
        z[2]='0'
    return x,y,z


'''
Global
''' 
#global
x=["","",""]
y=["","",""]
z=["","",""]
c=[]
print_board()

inputc(x,y,z)
print(c)
print_board()
inputh(x,y,z)
print(c)
print_board()
inputc(x,y,z)
print(c)
print_board()