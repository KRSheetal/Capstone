'''Part 2: List of classes

Write a program that asks for the names of all of the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line.'''


classes_list = [] #Initialise list to collect class names
class_name = input('Enter the class name.Press Enter to quit: ')  #ask user to enter the class name. And to press enter to break the loop

while class_name: #the class entered will be added to the list until the user quits

    classes_list.append(class_name) # adds the class enetred by the user to the List
    class_name = input('Enter the class name.Press Enter to quit: ') # Ask user to keep entering the class names until done

print (classes_list) # display classes

for x in classes_list: # display class from the list one per line
    print(x) # print one class per line

#to print the numbered list

for index, x in enumerate(classes_list): #prints with index one per line
    print(f'{index+1}. {x}') #prints a number and the class one per line starting from number 1 as index always starts from 0


