from dataclasses import dataclass

@dataclass #annotate dataclass here - dataclass is a decorator

class Student: #you do not need to add (self) in dataclass.
    #we do not need __init__ in dataclass as it's in-built
    #define string or float
    name: str 
    school_id: str
    gpa: float
  

#we do not need a __str__ in dataclass as it's in-built
#define string to print the formatted data 
''' def __str__(self): #traditional version
        return f'Name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}'
        '''

#define main function
def main():
    #add the data to the Student class
    alex = Student('Alex', 'Sg7424', 3.7)
    print(alex.name)
    print(alex.school_id)
    print(alex.gpa)
    print(alex)

#you can add any number of students' data
    sam = Student('Sam', 'De8472', 3.7)
    print(sam)

if __name__ == '__main__': #for multiple python files are imported into python file adding this line helps
    #python to run main from this(same) file
    main() #do not forget to call main function

#-----------------------------------
''' Traditional version VS dataclass version
1.You do not need to add (self) in dataclass.
2.This is more concise than the traditional version
3.This is more readable than traditional version
4.We do not need __init__ in dataclass as it's in-built
5.We do not need a __str__ in dataclass as it's in-built
6.The thing you need to remember is to import dataclass using 'from dataclasses import dataclass' and annotate @dataclass
'''
#------------------------------------


#traditional Class version
'''
class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA: {self.gpa}'

alex = Student('Alex', 'abcedf',3.9)
print(alex.name)
print(alex.school_id)
print(alex.gpa)
print(alex)

sam = Student('Sam', 'qwerty', 3.7)
print(sam)'''
