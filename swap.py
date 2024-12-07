'''
Swap Variables
Swap the values of two variables without using a third variable.
'''

'''
Psudocode
Okay lets make it just for innteger
so what im gonna do is take to variable
Either it can be integer or double 
so make a function and add the substract it from th eanother to make it swap itself'''


#making it infinite
while True:

#main
    print("Okay this swaping variable")
    print("You can input integer only")
    #input values
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    #brfore swapping
    print ("The values before swapping")
    print("a=",a)
    print("b=",b)
    #swapping without temporrary variable

    
    a=a+b
    b=a-b
    a=a-b

    #after swapping
    print("The values after swapping")
    print("a=",a)
    print("b=",b)

'''this concludes the program'''