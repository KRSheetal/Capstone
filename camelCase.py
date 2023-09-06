'''Part 3: camelCase

Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, 
and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output 
"fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a valid variable name. 
You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid 
characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code. '''

def banner():
   """Display program name"""
   message = 'Awesome camelCase program!'
   stars = '*' *len(message)
   print(f'\n{stars} \n{message} \n{stars} \n')


#define a function to convert the input sentence to camelCase
def sentence_to_camelCase(sentence): # 'This is a sentence' -- INPUT
    c = sentence.replace("-", " ").replace("_", " ") #remove all the '-' & '_' in a sentence
    c = c.split() #now split the sentence to words
    if len(sentence) == 0: #if no sentence entered exit the function return nothing
     return sentence #no sentence will be returned
    #if there is a sentence, convert first word to lower case and join the remaining words to the first word after capitalising the first letter 
    #of each word using title() and remove all the spaces between the words using replace()
    return c[0].lower() + ' '.join(c[1:]).title().replace(" ", "") # 'thisIsASentence' -- OUTPUT


#call the function here to convert the sentence to camel case
banner()
inputSentence = input('Enter sentence: ') #ask user to enter a sentence
camelCased = sentence_to_camelCase(inputSentence) #call the function with input sentencec
print(camelCased) #print the returned camel cased sentence



#Source: https://stackoverflow.com/questions/60978672/python-string-to-camelcase
   

