# TRY IT YOURSELF
#2-3 Personal Message

person = "Eric"
message = '"Hello {}, would you like to learn some Python today?"'.format(person)

print(message)

#2-4 Name Cases
# Use a Variable to represent a person's name, and then print that person's name in
# lowercase,uppercase, and title case.
name = "azhari ramadhan"
name_low = "{}".format(name.lower())
name_up = "{}".format(name.upper())
name_title = "{}".format(name.title())

print(name_low,name_up,name_title)

#2-5 Famous Quote

famous_ppl = "Kurt Cobain"
quote = "Saya lebih suka dibenci karena diriku, dari pada dicintai karena bukan diriku"
fms_quote = "{} pernah berkata, '{}'".format(famous_ppl, quote)

print(fms_quote)