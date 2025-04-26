### A ###
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)


### B ###
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a)

### C ###
name = "John"
name_2 = "Andrey"
print(type(name))
print(type(name_2))

### D ### Code with issue
my_number = 5 + 5
# Issue: we can't concatenate string and integer
# print("result is " + my_number)
# Fixed code:
print("result is:" + str(my_number))
print(f"result is: {my_number}")

### E ###
x = 5
y = 2.36
print(
    x + int(y)
)  # The result is 7 because we convert y to integer and then add it to x, when we use int() we truncate the decimal part

### Challenge ###
a = 8
b = "123"
# 1 Convert b to integer
print(a + int(b))
# 2 Convert a to string
print(str(a) + b)
