### A ###
x, y = 10, 68
if x > y:
    print("x is bigger then y")
else:
    print("y is bigger then x")
print("---")
### B ###
# For loop 5 times
for i in range(5):
    print("Iteration", i)
print("---")
for i in range(0, 5):
    print("Iteration number", i)
print("---")

### C ###
num = 4
if num == 1:
    print("Summer")
elif num == 2:
    print("Winter")
elif num == 3:
    print("Fall")
elif num == 4:
    print("Spring")
else:
    print("Invalid number")
print("---")

### D ###
count = 1
while count < 11:
    print(count)
    count += 1
print("---")

### E ###
age = 30
first_letter = "A"
currency = 3.5
is_flew = True
apartment_number = 123

print(type(age))
print(type(first_letter))
print(type(currency))
print(type(is_flew))
print(type(apartment_number))
print(age + currency)
print("---")


### F ###
def ask_for_phone_number():
    phone_number = input("Please enter your phone number: ")
    print(f"Phone number is: {phone_number}")


### G ###
def print_hello():
    print("Hello")


def calculate_sum():
    a = 5
    b = 3.2
    return a + b


### H ###
def print_name(name):
    print(f"Hello {name}")


def print_and_divide(number):
    print(number / 2)


### I ###
def sum_of_two_numbers(a, b):
    return a + b


def string_concatenation_with_space(str1, str2):
    return str1 + " " + str2


def get_number_from_user():
    return int(input("Please enter a number: "))


def get_number_from_user_and_modufy(number=get_number_from_user()):
    digits = []
    for i in str(number):
        digits.append(int(i))
    print(sum(digits))


get_number_from_user_and_modufy()


### Challenge ###
# Nested for loop > pyramid shape
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print("---")

### Challenge 2 ### > Diagonal
n = 7
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

print("---")
