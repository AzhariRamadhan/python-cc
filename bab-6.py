#6-1 Person
#   Use a dictionary to store information about a person you know.
#   Store their first name, last name, age, and the city in which they live. You
#   should have keys such as first_name, last_name, age, and city. Print each
#   piece of information stored in your dictionary.

person_information = {
    'first_name': 'ucok',
    'last_name': 'karo',
    'age': '69',
    'city': 'bengkulu',
}

first_name = person_information['first_name'].title()
print("His First Name is {}").format(first_name)

last_name = person_information['last_name'].title()
print("His Last Name is {}").format(last_name)

age = person_information['age']
print("His Age is about {} years old").format(age)

city = person_information['city'].title()
print("His live at {}").format(city)

#6-2. Favorite Numbers: 
print("\n6-2 Favorite Numbers:")

favorite_numbers = {
    'edo': '13',
    'edi': '9',
    'ade': '57',
    'adi': '69',
    'aldo': '77',
}

number = favorite_numbers['edo']
print("Edo favorite number is {}").format(number)

number = favorite_numbers['edi']
print("Edi favorite number is {}").format(number)