### A ###

# The error is: ZeroDivisionError: division by zero
# a = 1 / 0

try:
    a = 1 / 0
except ZeroDivisionError as e:
    print("The error is:", e)

print("---")

# Check if this code correct
try:
    x = 1

finally:
    print("Finally block")


### Writing to a file ###
with open(
    "test.txt", "w"
) as f:  # w = write mode, creates the file if it doesn't exist or overwrites it if it does
    f.write("Hello, world!\n")
    f.write("Hello, world!\n")


with open("test.txt", "r") as f:  # r = read mode, reads the file
    content = f.read()
    print(content)


# Exercise 1: Write to-do list #
def add_task():
    for i in range(3):
        task = input("Enter a task name:")
        with open("to-do-list.txt", "a") as f:
            f.write(task + "\n")


# Exercise 2: Read to-do list #
def read_task():
    with open("to-do-list.txt", "r") as f:
        for line in f:
            print(f"Task {line.strip()}")


# add_task()
# read_task()

### Strip ###

# Strip is used to remove whitespace from the beginning and end of a string
# It can be used with a string or a list

text = "   Hello, world!   "
print(text)
print(text.strip())


### with ###
# with handles opening and closing resources like files automatically, so you don’t forget to close them.

### Python Dictionary ###
# A dictionary is a collection of key-value pairs
# It is unordered, mutable and indexed
person = {
    "name": "Andrey",
    "age": 25,
    "city": "Tel Aviv",
}

print(person["name"])
print(person["age"])

# Modify #
person["age"] = 30
person["city"] = "Moscow"
print(person)

# Adding new values #
person["gender"] = "male"
print(person)

# Removing values #
del person["gender"]
print(person)

# Loop through a dictionary #
for key, value in person.items():
    print(f"{key}: {value}")

# only keys #
for key in person.keys():
    print(key)

# only values #
for value in person.values():
    print(value)

# Check if a key exists #
if "name" in person:
    print("Name is a key in the person dictionary")

# Check if a value exists #
if "Tel-Aviv" in person.values():
    print("Tel-Aviv is a value in the person dictionary")
else:
    print("Tel-Aviv is not a value in the person dictionary")

# Get the length of a dictionary #
print(len(person))

# Clear a dictionary #
person.clear()
print(person)


# Exercise 1:
my_dict = {
    "name": "Yossi-Choen",
    "age": 40,
    "favorite_language": "Python",
}
print(my_dict)
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Exercise 2
my_dict["age"] = 45
print(my_dict["age"])
