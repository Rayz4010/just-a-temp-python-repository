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

word=str(input("Enter the word you want to check palindrome on "))
rev_word=word[::-1]
if word==rev_word:
    print("The word:",word," is palindrome")
else:
    print("The word:",word," is not palindrome")

'''this concludes the end of the program
well this was was a little difficult'''