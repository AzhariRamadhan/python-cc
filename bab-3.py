#3-1 Names
# Store the name of a few of your friends in a list called names.
# Print each person`s name by accessing each element in the list, one at a time

names = ['ucok', 'budi', 'sukinem', 'lucinta luna', 'dedy']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3-2 Greetings
# Start with the list you used in Exercise 3-1, but instead of just printing each person`s name,
# Print a message to them.
# The text of each message should be the same, but each massage should be personalized with the person's nameself.

massage = "nama asli {[3]} adalah muhammad fatah".format(names)
print(massage)