"Calculating Numbers with Functions"

# variablename = functioname(param[,param]) This is a common syntax for python functions
# Inside the parentheses you may pass 1 or more values (called parameters) to the function

# The abs() function accepts 1 number and returns the absolute value of that specific number

x = -4
y = abs(x)
print(x)
print(y)

# Some functions may accept 2 or more values, e.g. the round() function takes 1 number as its first argument. The second argument
# is the number of decimal places to which you want to round that number, e.g. "2" for 2 decimal places

x = 1.23456789098765432100000000000000000000001
y = round(x,2)
print(x)
print(y, "\n\n")

# Some Built-In Python Functions for Numbers

"""
abs(x)               |  Returns the absolute value of a number x(converts negative numbers to positive)
bin(x)               |  Returns a string representing the value of x converted to binary
float(x)             |  Converts a string or number x to the float data type
format(x,y)          |  Returns x formatted according to the a pattern specified in y. This older syntax has been replaced with f-strings in current Python versions
hex(x)               |  Returns a string containing x converted to hexadecimal, prefixed with Ox
int(x)               |  Converts x to the integer data type by truncating (not rounding) the decimal portion and any digits after it
max(x, y, z, ...)    |  Takes any number of numeric arguments and returns whichever is the largest
min(x, y, z, ...)    |  Takes any number of numeric arguments and returns whichever is the smallest
oct(x)               |  Converts x to an octal number, prefixed with Oo to indicate octal
round(x, y)          |  Rounds the number x to y number of decimal places
str(x)               |  Converts the number x to the string data type
type(x)              |  Returns a string indicating the data type of x
"""

pi = 3.14159265358979
x = 128
y = -345.6789087
z = -999.9999
print("1:", abs(z))
print("2:", int(z))
print("3:", int(abs(z)))
print("4:", round(pi, 4))
print("5:", bin(x))
print("6:", hex(x))
print("7:", oct(x))
print("8:", max(pi, x, y, z))
print("9:", min(pi, x, y, z))
print("10:", type(pi))
print("11:", type(x))
print("12:", type(str(y)),"\n\n")

"Still more math functions"

# You can import more built-in functions using the math module, to do this put "import math" at the top of the file you're working on
# This makes the functions available to the rest of the code

# e.g. The sqrt() function gets the square root of a number, because its part of the math module, it cannot be used without importing the module first

# import math
# print(sqrt(81))

# If you do the following as was done above you will still get an error because you are treating sqrt() as a built-in function

"""To use a function from a module, you have to import the module and precede the function name with the module name and a dot.
Thus the module is called "math", and the function is called "sqrt" which leads to math.sqrt()
"""
import math
z = 81
print("sqrt function from module:", math.sqrt(z), "\n\n")

"Some Functions from the Python Math Module"

"""
math.acos(x)        |  Returns the arccosine of x in radians
math.atan(x)        |  Returns the arctangent of x, in radians
math.atan2(x,y)     |  Converts rectangular coordinates (x,y) to polar coordinates (r, theta)
math.ceil(x)        |  Returns the ceiling of x, the smallest integer greater than or equal to x
math.cos(x)         |  Returns the cosine of x radians
math.degrees(x)     |  Converts angle x from radians to degrees
math.e              |  Returns the mathematical constant e(2.718281...)
math.exp(x)         |  Returns e raised to the power x, where e is the base of natural logarithms
math.factorial(x)   |  Returns the factorial of x
math.floor()        |  Returns the floor of x, the largest integer less than or equal to x
math.isnan(x)       |  Returns True if x is not a number; otherwise returns False
math.log(x, y)      |  Returns the logarithm of x base y
math.log2(x)        |  Returns the base-2 logarithm of x
math.pi             |  Returns the mathematical constant pi(3.14159...)
math.pow(x, y)      |  Returns x raised to the power y
math.radians(x)     |  Converts angle x from degrees to radians
math.sin(x)         |  Returns the sine of x, in radians
math.sqrt(x)        |  Returns the square of root x
math.tan(x)         |  Returns the tangent of x radians
math.tau()          |  Returns the mathematical constant tau(6.283185...)

The constants pi,e and tau are unusual for functions in that you don't use parentheses.
"""


import math
pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454

print("1:", pi)
print("2:", e)
print("3:", tau)
print("4:", math.sqrt(x))
print("5:", math.factorial(y))
print("6:", math.floor(z))
print("7:", math.degrees(y))
print("8:", math.radians(45), "\n\n")

"Formatting Numbers"

# Formatting with f-strings
# Format strings or f-strings are the easiest way to format data, all you need is a lowercase f or uppercase F followed immediately
# by some text or expressions enclosed in quotation marks.

# e.g. f"Hello {username}"

"""The f before the first quotation mark tells python that what follows is a format string, inside quotation marks, the text, called
the literal part, is displayed literally (exactly as typed into the f-string). Anything in curly braces is the expression part of
the f-string, a placeholder for what will appear when the code executes.
"""

username = "Alan"
print(f"Hello {username}", "\n\n")

unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}", "\n\n")


"Showing dollar amounts"

# In order to get commas for the thousands, we need a colon and a comma inside the closing curly brace {:,}

print(f"New Subtotal: ${quantity * unit_price :,}", "\n\n")

# To get pennies to show as 2 digits, follow the comm with .2f

print(f"Final Subtotal: ${quantity * unit_price:,.2f}", "\n\n")


"Formatting percent numbers"

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}", "\n\n")

# To get the percentage instead of doing .2f we do .2% (multiplies number by 100 to get percentage)

print(f"Sales Tax Rate percent {sales_tax_rate: .2%}", "\n\n")

# We used 2 decimal placed for .2f, however we can choose whichever amount of decimal places we need for precision

print(f"Sales Tax Rate 1 decimal {sales_tax_rate: .1%}", "\n\n")

print(f"Sales Tax Rate 9 decimal {sales_tax_rate: .9%}", "\n\n")


# Doesn't matter what kind of quotations you use

sales_tax_rate = 0.065
sample1 = f'Sales Tax Rate single quotations {sales_tax_rate: .2%}'
sample2 = f"Sales Tax Rate double quotations {sales_tax_rate: .2%}"
sample3 = f'''Sales Tax Rate triple single quotations {sales_tax_rate: .2%}'''
sample4 = f"""Sales Tax Rate triple double quotations {sales_tax_rate: .2%}"""

print(sample1)
print(sample2)
print(sample3)
print(sample4, "\n\n")


"Making multiline format strings"

# We can use \n in order to make a line break, don't forget to put 'n in the literal portion of the format string, not in the curly braces

user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output = f"{user1} \n{user2} \n{user3}"
print(output, "\n\n")

# If you use triple quotation marks you don't need to use \n you can just break the line in the format string wherever you want it to break in the ourput


unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total:     ${total:,.2f} \n\n
"""
print(output)


"Formatting width and alignment"

# You can also control the width of the output (and alignment of content within that width) by following the colon in the f-string
# with < (for left aligned), ^ (for centered), or > (for right aligned). e.g. :>20, this will make the output 20 characters wide

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal width:  ${subtotal:>9,.2f}
Sales Tax width: ${sales_tax:>9,.2f}
Total width:     ${total:>9,.2f} \n\n
"""
print(output)

# Because the dollar signs which are part of the literal are outside of the curly brackets, it is not affected by the >9 after the
# colon.

# We can only use .2f on a number, but we can't attach $ to a number without making it a string, but then .2f wouldn't work,
# therefore

s_subtotal = "$" + f"{subtotal:,.2f}"



"Working with common string operators"

# When working with strings, the first character counts as 0, not 1
# e.g. ABCDE = 01234, the last character of this string is 4 since the first character is 0

"Python Sequence Operators That Work with Strings"

"""
x in s                 |  Returns True if x exists somewhere in string s
x not in s             |  Returns True if x is not contained in string s
s * n or n * s         |  Repeats string s n times
s[i]                   |  The i th item of string s where the first character is 0
s[i:j]                 |  A slice from the string x beginning with the character at position i though the character at position j
s[i:j:k]               |  A slice of s from i to j with step k
min(s)                 |  The smallest (lowest) character of string s
max(s)                 |  The largest(highest) character of string s
s.index(x[, i[, j]])   |  The numeric position of the first concurrence of x in string s. The optional i and j restrict the search to the characters from i to j
s.count(x)             |  The number of times string x appears in larger string s
"""

s = "Abracadabra Hocus Pocus you're a turtle dove"

# Is there a lowercase letter t contained in s?
print("1:", "t" in s)
# Is there an uppercase letter t contained in s?
print("2:", "T" in s)
# Is there no uppercase T in s?
print("3:", "T" not in s)
# Print 15 hyphens in a row
print("4:", "-" * 15)
# Print the first character in string x
print("5:", s[0])
# Print characters 33 - 39 from string x
print("6:", s[33:39])
# Print every third character in string s starting at 0
print("7:", s[0:44:3])
# Print lowest character is s (a space is lower than the letter a) The ranking is based on the ASCII number of each character
print("8:", min(s))
# Print the highest character in s
print("9:", max(s))
# Where is the first uppercase p?
print("10:", s.index("P"))
# Where is the first lowercase O in the latter half os string s
# Note that the returned value still starts counting from 0
print("11:", s.index("o",22,44))
# How many lowercase letters a are in string s?
print("12:", s.count("a"))

"""When working with ASCII in python you can use the ord() function which takes a character as input and returns the ASCII number
   of that character.
   
   e.g. print(ord("A")) returns 65 due to the ASCII chart
   
   The chr() function does the opposite, you give it a number and it returns the ASCII character for that number.
   
   e.g. print(chr(65)) returns A due to the ASCII chart

"""

"Manipulating strings with methods"