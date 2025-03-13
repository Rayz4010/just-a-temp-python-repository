import random
'''
FUNCTIONS
'''
'''
Psudocode:
first just taking 3 list
each have 3 value where the use can modify
make a computer which can randomly generate a number
make sure the user and computer doest not conflict 
give the winning and drawing conditions 
a main function giving one chance and ready to call other
'''
#rules
def rules():
    print("0|1|2\n3|4|5\n6|7|8")
    print("the above is the table")
    print("You have to enter the position between 0-8")
    
#for printing board
def print_board():
    print()
    print(x)
    print(y)
    print(z)
    print()

#human logic
def checkh(ing):
    if ing<=8:
        if ing in c:
            print("Already filled")
            inputh(x,y,z)
        else:
            c.append(ing)
    else:
        print("Invalid input")
def inputh(x,y,z):
    inh=int(input("Enter the position between 0-8: "))
    checkh(inh)
    #if inh>0 and inh<=2:
    if inh==0:
        x[0]="X"
    if inh==1:
        x[1]='X'
    if inh==2:
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
    
#computer logic
def checkc(inp):
    if inp in c:
        inp=random.randint(0,8)
        checkc(inp)
    else:
        c.append(inp)
def inputc(x,y,z):
    inp=random.randint(0,8)
    checkc(inp)
    if inp==0:
        x[0]="0"
    if inp==1:
        x[1]='0'
    if inp==2:
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
Game Logic
'''


#conditions
def winning_condition():
    cond=False
    if x[0]==x[1]==x[2]=='X' or y[0]==y[1]==y[2]=='X' or z[0]==z[1]==z[2]=='X' or x[0]==y[0]==z[0]=='X' or x[1]==y[1]==z[1]=='X' or x[2]==y[2]==z[2]=='X' or x[0]==y[1]==z[2]=='X' or x[2]==y[1]==z[0]=='X' or x[0]==y[1]==z[2]=='X' or x[2]==y[1]==z[0]=='X':
        print("You win")
        cond=True
        check_winning_condition(cond)
    elif x[0]==x[1]==x[2]=='0' or y[0]==y[1]==y[2]=='0' or z[0]==z[1]==z[2]=='0' or x[0]==y[0]==z[0]=='0' or x[1]==y[1]==z[1]=='0' or x[2]==y[2]==z[2]=='0' or x[0]==y[1]==z[2]=='0' or x[2]==y[1]==z[0]=='0' or x[0]==y[1]==z[2]=='0' or x[2]==y[1]==z[0]=='0':
        print("Computer wins")
        cond=True
        check_winning_condition(cond)
    elif x[0]!='' and x[1]!='' and x[2]!='' and y[0]!='' and y[1]!='' and y[2]!='' and z[0]!='' and z[1]!='' and z[2]!='':
        print("Board filled ")
        exit()
    else:
        print("Draw")
        cond=False
        check_winning_condition(cond)       
def check_winning_condition(cond):
    if cond==True:
        exit()
def check_board_full():
    if len(x)==3 and len(y)==3 and len(z)==3:
        print("Board full")
        exit()
    
        
#main       
def main():
    i=0
    while i==0:
        inputh(x,y,z)
        print_board()
        winning_condition()
        print(c)
        inputc(x,y,z)
        print_board()
        winning_condition()
        print(c)
        
'''
Global
''' 
#global
x=["","",""]
y=["","",""]
z=["","",""]
c=[]
rules()
print_board()
main()
print(len(x))

'''this concludes the program'''