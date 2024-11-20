'''
FizzBuzz
Print numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers divisible by both, print "FizzBuzz".
'''

''' okay here the question is clear so lets get to coding'''

# taking a for loop for 1 to 100
for i in range(1,101):
    if i%3==0:
        print("Fizz")
        #adding continue to skip this iteration
        continue
    if i%5==0:
        print("Buzz")
        #samre as before
        continue
    #printing the iteration
    print(i)
'''
this concudes the program
'''