# Variables
# Assign x the value of 5
x = 5
# x is a container containing the value of 5
# x is a variable

print(x)

#  Data types
#  1. Numbers 
#  Example 2
y = 6
z = x + y

print(z)

# Check the class/type of data/variable
print(type(x))

# Operations on Numbers
# Arithmetic Operatos () ** * / + -
b = 3 + 5 * 4 / 16 -1
print(b)

#  Dynamic Typing $ Restriction of Data Types
# Without declaring the below, we will be using dynamic typing
# How to solve this syntax error!??
# int c; 

c = 6
c= 13

#  Restricticting the variable c to integers
#  Below results to a SyntaxError: invalid syntax
# c = "dev"
print(c)

# Casting
x = 2
type(x) #prints int

#  To cast {change the data type of a variable}
x = float(2)
type(x) #prints float


# 2. Strings
# Methods
d = "water"

d.upper()

# Check the functions related to a variable type
dir("string")

#  Indexing and
i = "water"
i[2]  # Returns 't'

j = "ivan musebe"
j.replace("m", "M")
j.replace(j[0], j[0].upper())

# Slicing
j[:4] # Returns ivan


#  String formatting
x = "is"
y = "my"
z = "name"

#  Method 1
p = y + " " + x + " " + z
print(p)

#  Method 2
x = "My name is"
y = "Ivan"
z = "My name is {}".format(y)

#  Also written
z = f"My name is {y}"

print(z) # 'My name is Ivan'

# For a list
q = ["Ivan", "coding", 27]
z = f"My name is {q[0]} and I love {q[1]}. I am {q[2]} years old."
print(z)


# 3. Lists
x = ["red", "blue", "green", "yellow", "black"]
print(x)

# Has same indexing as strings
x[2] # Returns green

# Length; How many elements does the list have?
len(x) # Returns 5

# Adding and remove elements in a list.
x.append("pink")
x.remove("yelkow")

# 4. Tuple. Contained in brackets
x = ("red", "blue", "green", "yellow", "black")
x[2] # Returns green

# 4. Dictionary {}
x = {
    "number":1,
    "name":"blue",
    "age":27
}

# Return name
x["name"] # Value: blue

# Replace
x["name"] = "Ivan"

# Add and remove value
x["yoe"] = 5
x.pop("age") # Remove an item

# Remove the last item
x.popitem()

# 5. Boolean
5<6 # True
4>5 # False