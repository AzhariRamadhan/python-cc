#7-1 Rental Car
#car = input("Please tell us the car names you wanted: ")
#print("\nLet me see if i can find you {}".format(car))

#7-2 Restaurant Seating
print("\nRestaurant Seating")

number = input("Enter a number how many people in dinner group: ")
number = int(number)

if number > 8 :
    print("\nyou have to wait for {} table".format(number))
else:
    print("\n{} tbale is ready".format(number))

#7-3
print("\n#7-3")

number1 = input('give me a number: ')

if int(number1)%10 == 0:
    print('Number is a multiple of 10')
else:
    print('Number is not a multiple of 10')

#7-4
print('\n#7-4')

topping = ''
prompt = 'What topping would you like on your pizza? '

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print('Adding ' + topping + ' to your pizza')

#7-5 Movie Tickets
print('\n#7-5 Movie Tickets')

age = ''
promptTicket = 'How old are you?'
#active = True #<--- untuk soal 7-6 silahkan hapus tanda '#' sebelum active

# untuk soal 7-6 'while age di ganti dengan 'while active == True:'
while age != 'cancel':
    age = input(promptTicket)
    if age == 'cancel':
        break
    age = int(age)
    if age < 3:
        print('Your Ticket is free')
    elif age < 12:
        print('Your Ticket costs Rp. 15.000')
    else:
        print('Your Ticket costs Rp. 35.000')

#7-7 infinity
print('\n#7-7 infinity loop')
i = 1

while i > 0:
    i = i + 1
    print(i)

#7-8 Deli
print('\n#7-8 Deli')

sandwich_orders = ['meet', 'cheese', 'pasta', 'sosis', 'tempoyak', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich.pop()
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('All these sandwiches were made: ')
print(str(finished_sandwiches))

#7-9 
print('\n#7-9')

sandwich_orders = ['pastrami', 'reuben', 'pastrami', 'blt', 'pastrami', 'ham and cheese']
finished_sandwiches = []

print('We\'re all out of pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        continue
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('All these sandwiches were made: ')
print(str(finished_sandwiches))

#7-10 Dream Vocation
print('\nDream Vocation')

active = True
places = []

while active:
    place = input('If you could visit one place in the world, where would you go? ')
    places.append(place)
    repeat = input('Would you like to add more places? ')
    if repeat != 'no':
        continue
    active = False

print('Places you would like to go: ')
print(str(places))