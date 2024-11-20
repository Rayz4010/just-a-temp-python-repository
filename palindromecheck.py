'''
Palindrome Check
Check if a given string is a palindrome (reads the same backward as forward).
'''

'''okay lets check the palindrome
first taking a string
reversing it
checking the conditioj is true
peinting result'''

'''wow the overviwew was pretty brief'''
#taking input
word=str(input("Enter the word you want to check palindrome on "))
'''
okay so here let me break it down
[]- wahts this- the indexing box
[:]= giving this is go though it from index 0 to index n
[::-1]- giving another : followed by a value is now of steps to jump in the list
now indicationg postive or negative is wethere it will go in reverse or foeward
generally pos is forward and negative is reverse
'''
rev_word=word[::-1]


if word==rev_word:
    #checking if the contition is true
    print("The word:",word," is palindrome")
else:
    print("The word:",word," is not palindrome")

'''this concludes the end of the program
well this was was a little difficult'''