#4-1
pizzas = ['pepperoni', 'deluxe', 'mushrooms and pepperoni', 'meat lovers']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')
print('I really love pizza!')

#4-2
animals = ['cat', 'dog', 'chinchilla']
for animal in animals:
    print('A ' + animal + ' would make a great pet.')
print('ANy of these animals would make a great pet!')

#4-3
for number in range(1, 21):
    print(number)

#4-4
numbers = [v for v in range(1, 1000001)]

for number in numbers:
    print(number)

#4-5
numbers = [v for v in range(1, 1000001)]

print('Min: ' + str(min(numbers)))
print('Max: ' + str(max(numbers)))

print('Sum: ' + str(sum(numbers)))

#4-6
numbers = [v for v in range(1, 21, 2)]

for number in numbers:
    print(number)

#4-7
numbers = [v for v in range(3, 31, 3)]

for number in numbers:
    print(number)

#4-8
cubes = [v**3 for v in range(1,11)]

for cube in cubes:
    print(cube)

#4-9
cubes = [v**3 for v in range(1,11)]

for cube in cubes:
    print(cube)

#4-10
numbers = [v for v in range(3, 31, 3)]

print(numbers)
print('The first three items in the list are: ' + str(numbers[:3]))
print('Three items from the middle of the list are: ' + str(numbers[4:7]))
print('The last three items in the list are: ' + str(numbers[-3:]))

#4-11
pizzas = ['pepperoni', 'deluxe', 'mushrooms and pepperoni', 'meat lovers', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append('four cheese')
friend_pizzas.append('heart of artichoke')

print('My favorite pizzas are: ' + str(pizzas))
print('My friend\'s favorite pizzas are: ' + str(friend_pizzas))

#4-12
pizzas = ['pepperoni', 'deluxe', 'mushrooms and pepperoni', 'meat lovers', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append('four cheese')
friend_pizzas.append('heart of artichoke')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print('My friend\'s favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)

#4-13
foods = ('bread', 'water', 'salad', 'spaghetti', 'ice cream')

for food in foods:
    print(food)

# foods[0] = 'chicken'

foods = ('bread', 'water', 'salad', 'sushi', 'tacos')

for food in foods:
    print(food)