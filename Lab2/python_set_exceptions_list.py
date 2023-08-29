
#sets - sets are unordered

cats = set() #create empty set

cats.add('Lion')
cats.add('Tiger')

print(cats)
cats.add('Cheetah')
print(cats) #they are unordered

cats.add('Tiger')
print(cats) #doesn't allow duplicates

birds = {'owl', 'parrot', 'crow'} #create set

birds.remove('owl')
birds.add('pegion')
print(birds)

for bird in birds:
    print(bird)

bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'eagle', 'parrot'] # create a list
print(bird_list) # allows duplicates

#to remove duplicates, convert the List to the Set and the back into the List as set removes the duplicates
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)
