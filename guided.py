# declare a variable
name = "Robert"

#print the var
print(name)


p = [10, 60, 20, 5, "Banana"]
print(p)
p.append(77)
print(p)

#Loop over list P and print every element
#for every element in P do some sort of code
for element in p:
    print(element)

# lets print the index and the element at the index of P
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]}')\


#UNIQUE TO PYTHON 
#List Comprehensions
# another way to create a list
numbers = [1, 4, 9, 16, 25]
#create another list of squares from the numbers list
#this is the long way of doing this list
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# lets use list comprehensions to redu this list!
#for each element from numbers multiply by itself and add to cooler_squares
cooler_squares = [num*num for num in numbers]
print(cooler_squares)

#lets create a list of just even numbers from our numbers list
evens = [num for num in numbers if num % 2 == 0]
print(evens)

names = ["Sarah", "Jarah", "Sandy", "Sam", "Shawn", "Bob", "Robert"]
#create a new list containing only names with S
#all names should be capitalized
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)



#dictionaries!
# / maps / hashmaps / objects blah
#a key -> value datastructure

new_dict = {}

#create a dictionary with some keys and values
food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a veggi'
}

print(food_dict)

#lets add a new key value pair
food_dict['cucumber'] = 'is maybe a veggi?'
print(food_dict)

#access and print 
choosen_food = 'apple'
print(food_dict[choosen_food])

#iterate through the keys and the values of a dictionary
#for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

#does something exist in a dictionary?!
#is apple in food dict
print('apple' in food_dict)
print('banana' in food_dict)

# Tuples and Sets
# Tuples
tup = (1,2,3,4)
#now this tuple CANT BE CHANGED
for item in tup:
    print(item)

#access particular elem
print(tup[1])

#you cannot modify tup in any way
#tup[1]= 'newthing'

# Sets are basically dictionaries without values!
fruit = {'cucumber', 'apple', 'banana'}
fruit.add('pizza')
for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I dont think cucumber is a fruit")