# This is a Python comment in my first Python app.
# This variable contains an integer
quantity = 10
# quantity = 14
# This variable contains a float
unit_price = 1.99
# unit_price = 26.99
# This variable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
# Show the results
print(f"The extended price is: {extended_price}")

"""This is a multiline comment in Python
This type of comment is sometimes called a Docstring.
A docstring starts with 3 double-quotation marks, and also ends with 3
    double quotation marks. """

print("Hello World")

print("Hi there, I am a string\n"
      'Hello World\n'
      "123 Oak Tree Lane\n"
      "(267)555-1234\n"
      "18902-3384")

# If a string contains an apostrophe (single quote), the entire quote should be enclosed in double quotation marks:

print("Mary's dog said Woof!")

# If a string contains double quotation marks make sure to enclose the entire thing is single quotation marks:

print('The dog of Mary said "Woof".')

# In order to escape (ignore) a character, just precede it with a backslash(\)

print('Mary\'s dog said "Woof"')

print("Mary's dog said \"Woof\".")

# Another common use of backslash is (\n) to add a line break for the user

print("The old pong\nA from jumped in, \nKerplunk!")
