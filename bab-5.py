#5-1 Coditional test

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? i predict False.")
print(car == 'audi')

#5-3 Alien Colors
print('\n5-3 Alien Colors')
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("The Player earned 5 points")
elif 'yellow' in alien_color:
    print("The Player not earned anything")
elif 'red' in alien_color:
    print("The Player not earned anything")

print("\nThe Player Passes the game")

#5-4 Alien Color Part 2
print("\nAlien Color Part 2")

if 'green' in alien_color:
    print("Player earned 5 point")
if 'yellow' in alien_color:
    print("Player earned 10 point")
if 'red' in alien_color:
    print("Player earned 10 point")

#5-4 Alien Color Part 2 Else block
print('\n5-4 Else Block')
color_alien = 'red'

if 'yellow' in color_alien:
    print("Player earned 5 Point")
else:
    print("Player earned 10 Point")

#5-5 Alien Colors part 3
# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain
print("\n5-5 Alien Color part 3")

if 'green' in color_alien:
    print("Player earned 5 point")
elif 'yellow' in color_alien:
    print("Player earned 10 point")
else:
    print("Player earned 15 point")
    
#5-6
age = 15

if age < 2:
    print('The person is a baby')
elif age >= 2 and age < 4:
    print('The person is a toddler')
elif age >= 4 and age < 13:
    print('The person is a kid')
elif age >= 13 and age < 20:
    print('The person is a teenager')
elif age >= 20 and age < 65:
    print('The person is an adult')
else:
    print('The person is an elder')

#5-7 Favorite Fruits
favorite_fruits = ['banana', 'nectarine', 'peach', 'pears', 'apples']

if 'banana' in favorite_fruits:
    print('You really like bananas!')

if 'peach' in favorite_fruits:
    print('You really like peaches!')

if 'cantaloupe' in favorite_fruits:
    print('You really like cantaloupe!')

if 'watermelon' in favorite_fruits:
    print('You really like watermelon!')

if 'pears' in favorite_fruits:
    print('You really like pears!')

#5-8 Hello Admin
print("\n5-8 Hello Admin")

list_names = ['admin', 'budi', 'lucinta luna', 'dedy', 'young lex', 'ria ricis']

user_logins = ['admin', 'jaden']

for user_login in user_logins:
    if user_login in list_names:
        print("Hello {}, would you like to see a status report").format(user_login)
    else:
        print("Hello {}, thank you for logging in again").format(user_login)
        
#5-10
current_users = ['admin', 'winston', 'ashley', 'eric', 'martin', 'ben']
new_users = ['Winston', 'ashley', 'dianne', 'xia', 'calvin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('You will need to enter a new username')
    else:
        print('The username is available')
        
#5-11
numbers = [v for v in range(1, 10)]
ordinal_suffix = ''

for number in numbers:
    if number == 1:
        ordinal_suffix = 'st'
    elif number == 2:
        ordinal_suffix = 'nd'
    elif number == 3:
        ordinal_suffix = 'rd'
    else:
        ordinal_suffix = 'th'
    print(str(number) + ordinal_suffix)
