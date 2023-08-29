#tuples

city_state = [('Seattle', 'WA'), ('Portland','OR'),('San Fransisco', 'CA'),]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

print('-----------------')
#tuples can also do  this
#unpacks each individual when seperated with commas

city, state = first_city_state
print(city)

animals = ('lion', 'puma', 'cheetah')

lion, puma, cheetah = animals
print(cheetah)

#get distance using tuple
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances) #prints tuple

print(distances[0])

miles, km = get_distance()
print(miles)


#useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'tiger', 'stripes', #return a tuple

#unpack your tuple to conveniently get both values in seperate variable 
cat, pattern = get_random_cat_and_pattern()

#if you prefer you can do this but it's usually more work
data = get_random_cat_and_pattern()
print(data[0]) #prints tiger

#error handling

try:
    print(data[10])
except:
    print('oops, that does not exist.')