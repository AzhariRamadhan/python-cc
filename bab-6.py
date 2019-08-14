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

#6-3
glossary = {
    'if statements': 'conditional statements, conditional expressions and conditional constructs are features of a programming language, which perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to true or false.',
    'loops': 'A loop is a sequence of statements which is specified once but which may be carried out several times in succession.',
    'variable': 'a variable or scalar is a storage location (identified by a memory address) paired with an associated symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value.',
    'dictionary': 'an abstract data type composed of a collection of (key, value) pairs, such that each possible key appears at most once in the collection',
    'list': 'an abstract data type that represents a countable number of ordered values, where the same value may occur more than once',
}

print('If Statements: \n\t' + glossary['if statements'])
print('Loops: \n\t' + glossary['loops'])
print('Variables: \n\t' + glossary['variable'])
print('Dictionary: \n\t' + glossary['dictionary'])
print('List: \n\t' + glossary['list'])

#6-4
glossary = {
    'if statements': 'conditional statements, conditional expressions and conditional constructs are features of a programming language, which perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to true or false.',
    'loops': 'A loop is a sequence of statements which is specified once but which may be carried out several times in succession.',
    'variable': 'a variable or scalar is a storage location (identified by a memory address) paired with an associated symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value.',
    'dictionary': 'an abstract data type composed of a collection of (key, value) pairs, such that each possible key appears at most once in the collection',
    'list': 'an abstract data type that represents a countable number of ordered values, where the same value may occur more than once',
}

for term, definition in glossary.items():
    print(term.title() + ': \n\t' + definition)
    
#6-5
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'khwae yai': 'thailand',
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'winston': 'go',
    'eric': 'javascript',
    'ben': 'javascript',
    'martin': 'javascript',
}

should_take_list = ['martin', 'jen', 'ashley', 'sameer', 'david']

for name in should_take_list:
    if name in favorite_languages.keys():
        print('Thanks for responding')
    else:
        print('Please take the poll')

#6-7
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'winston': 'go',
    'eric': 'javascript',
    'ben': 'javascript',
    'martin': 'javascript',
}

should_take_list = ['martin', 'jen', 'ashley', 'sameer', 'david']

for name in should_take_list:
    if name in favorite_languages.keys():
        print('Thanks for responding')
    else:
        print('Please take the poll')
        
#6-8
too_sweety = {
    'owners_name': 'Winston',
    'age': 12
}

belle = {
    'owners_name': 'Ashley',
    'age': 6
}

buffy = {
    'owners_name': 'Gary',
    'age': 2
}

pets = [too_sweety, belle, buffy]

for pet in pets:
    print(pet['owners_name'])
    print(pet['age'])

#6-9
favorite_places = {
    'winston': ['los angeles', 'seattle', 'portland'],
    'ashley': ['los angeles', 'hawaii', 'michigan'],
    'ben': ['los angeles', 'valley', 'san francisco'],
}

for name, places in favorite_places.items():
    print(name.title() + ': ' + str(places))

 #6-10
favorite_numbers = {
    'winston': [1, 2, 3],
    'ashley': [2, 3, 4],
    'ben': [3, 4, 5],
    'eric': [4, 5, 6],
    'sameer': [5, 6, 7],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + ': ' + str(numbers))
    
#6-11
cities = {
    'los angeles': {
        'country': 'usa',
        'population': '3.9 million',
        'fact': 'center of nation\'s film and television industry',
    },
    'san francisco': {
        'country': 'usa',
        'population': '864 thousand',
        'fact': 'center of nation\'s technology industry',
    },
    'casablanca': {
        'country': 'morocco',
        'population': '3.1 million',
        'fact': 'one of africa\'s largest financial centers',
    },
}

for name, info in cities.items():
    print(name.title() + ': ' + str(info))
    
#6-12
cities = {
    'los angeles': {
        'country': 'usa',
        'population': '3.9 million',
        'fact': 'center of nation\'s film and television industry',
    },
    'san francisco': {
        'country': 'usa',
        'population': '864 thousand',
        'fact': 'center of nation\'s technology industry',
    },
    'casablanca': {
        'country': 'morocco',
        'population': '3.1 million',
        'fact': 'one of africa\'s largest financial centers',
    },
}

for name, info in cities.items():
    print('The city of ' + name.title() + ' is in the country of ' + info['country'].title())
    print('\t' + 'It has a population of ' + info['population'])
    print('\tAn interesting fact is ' + info['fact'])
