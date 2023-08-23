'''Part 1: Hello, birthday month

Write a program that asks for your name and the month you were born in.

Then, your program should print
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in the current month
Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.'''

from datetime import date #import data and time from system


name = input('Please enter you name: ') #ask user to enter the name
birth_month = input('Please enter your birth month: ') #ask your to enter the birth month

now = date.today() # get the system's current date
current_month = now.month #extract month from system's current date. Note: The month will be in number
current_month = now.strftime('%B') #convert the month to a string

print(f'Hello, {name}!') #Greet the user with their name
print(f'You have {len(name)} letters in your name.') #display number of letters in users name

if birth_month.lower() == current_month.lower(): # convert to lowercase to compare the month entered by user and current month
    print('Happy birthday month!') #if month matches display this message



