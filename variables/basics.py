# 1. What is a Variable?
# A variable is a name that stores a value in memory.

x = 10
name = "Ali"


# 2. Creating Variables
# In Python, you do not need to declare type.

a = 5
b = 10
c = 3.14
name = "John"


# 3. Rules for Naming Variables
# ✔ Allowed:
# letters (a–z, A–Z)
# numbers (0–9) but not at start
# underscore (_)

my_var = 10
age1 = 20
_name = "Ali"

# ❌ Not allowed:
# 2name = "Ali"   # error
# my-var = 10     # error


# 4. Data Types in Variables

x = 10              # int
y = 3.14            # float
name = "Ali"        # string
is_active = True    # boolean


# 5. Multiple Assignment

a, b, c = 1, 2, 3

# Same value:
x = y = z = 100


# 6. Changing Variable Values

x = 10
x = 20
print(x)  # 20


# 7. Checking Type of Variable

x = 10
print(type(x))


# 8. User Input in Variables

name = input("Enter your name: ")
print(name)


# 9. Type Conversion (Casting)

x = "10"
y = int(x)

a = float("3.5")
b = str(100)


# 10. Why Variables are Important?
# Variables are used to:
# store data
# reuse values
# make programs dynamic
# perform calculations
# handle user input

a = 5
b = 10
print(a + b)


# 11. Best Practice
# ✔ Use meaningful names:

age = 20
student_name = "Rav"

# ❌ Avoid:
# a = 20
# x1 = "Rav"