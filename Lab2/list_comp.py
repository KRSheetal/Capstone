#the classes a student is registered for 
classes_registered = ['ITEC 1150','ITEC 1100','ENGL 1340','MATH 1100']

#make a list of only ITEC classes
only_itec = [c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)


#record temperature every day. Record -1 if not possible to take 
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

#make a list if numbers that represent a valid temperature measurement
only_real_measurment = [temp for temp in high_temps if temp != -1]
print(only_real_measurment)

#display in celcius
temp_celsius = [(temp_f -32) * 5/9 for temp_f in only_real_measurment]
print(temp_celsius)

#display average temperature
average = sum(temp_celsius)/len(temp_celsius)
print(f'The average is {average:.2f}')

#My turn to list comprehension
#write a list comprehension to make a new list with each number increased by one
this_list = [2, 4, 6]

#increased by one
increased_by_one = [(num + 1) for num in this_list ]
print(increased_by_one) #[3,5,7]

#Display numbers excluding 0 from the below list
numbers = [2,0,5,3,1,0,5,0,0]
no_zero = [n for n in numbers if n!=0]
print(no_zero) #[2, 5, 3, 1, 5]


#uppercase only if it is pizza
foods = ['cheese pizza', 'Veggie pizza','tacos', 'corn pizza']
pizzas = [food.upper() for food in foods if 'pizza' in food]
print(pizzas) #['CHEESE PIZZA', 'VEGGIE PIZZA', 'CORN PIZZA']

#make a new list with all the numbers doubled, but only if the number is not zero
number_list = [0, 10, 4, 3, 0, 20]
double_without_zero=[num*2 for num in number_list if num!=0]
print(double_without_zero) #[20, 8, 6, 40]