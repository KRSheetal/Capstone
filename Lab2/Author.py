
#create an Author class
class Author:
    def __init__(self, name):
        self.name = name 
        self.books = [] #initialise a list

    #add the books to books list
    def publish(self, title):
        #find if its a duplicate book
        if title in self.books:
            print(f'Book \'{title}\' already exists!') #if yes, show error message
        else:
            self.books.append(title) #if not, add the book to the list

#ignore below code. Below code counts the duplicates and makes a list of it and then remove the duplicate from the list.
#this is longer version of above -- if title in self.books:
    '''self.books.append(title)
        duplicate = [b for b in self.books if self.books.count(b)>1]
        if len(duplicate) != 0:
        print('Book', duplicate[0], 'already published!')
        self.books.remove(title)'''  

        
#for concise python coding instead of IF statement version
    def __str__(self):
        #add book with comma between each books added
        titles = ', '.join(self.books) or 'No published books' # data = a(truthy) or b(falsy)
        return f'Author: {self.name}, Books: {titles}' #print statement


#calls method and prints the data
def main():
    chetan_bhagat = Author('Chetan Bhagat')
    chetan_bhagat.publish('Five Point Someone')
    chetan_bhagat.publish('Half Girlfriend')
    chetan_bhagat.publish('Five Point Someone')
    chetan_bhagat.publish('One Indian Girl')
    chetan_bhagat.publish('2 States')
    
    print(chetan_bhagat) #prints the list of books

    rowling = Author('J. K. Rowling')
    rowling.publish('Harry Potter and the Philosopher\'s Stone')
    rowling.publish('Fantastic Beasts and where to Find Them')
    rowling.publish('Harry Potter and the Philosopher\'s Stone')
    print(rowling) #prints the list of books


main()

#---------OR try this-------------#

'''    def __str__(self):
        if self.books:
            books_list = ', '.join(self.books)
        else:
            books_list = 'No Books'
        return f'Name: {self.name} Books Published: {books_list}'

print('----------------------------------')
shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Richard III')

print(shakespeare)
print('----------------------------------')
sheetal = Author('Sheetal')
print(sheetal)
print('----------------------------------')'''






