quantity = 5
item_number = 150
price = 51

# using positional placeholders (*args)
order = 'We want {} pieces of item number {} for {:.2f} dollars'.format(quantity, item_number, price)
print(order)

# using indexed placeholders (*args)
order = 'We want {0} pieces of item number {1} for {2:.2f} dollars'.format(quantity, item_number, price)
print(order)

# using indexed placeholders more than once (*args)
age = 39
name = 'Joe'
text = "the player name is {1}. {1} is {0} years old.".format(age, name)
print(text)
