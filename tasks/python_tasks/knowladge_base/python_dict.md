
# 🧠 Python Dictionary Summary

A **dictionary** (`dict`) in Python is a collection of **key-value pairs**.

---

## ✅ Basic Example

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

---

## 🔹 Accessing Values

```python
print(person["name"])  # ➜ Alice
```

---

## 🔸 Modifying and Adding

```python
person["age"] = 31
person["email"] = "alice@example.com"
```

---

## ➖ Removing Keys

```python
del person["city"]
```

---

## 🔁 Looping Through Dictionary

```python
for key in person:
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🧪 Common Methods

| Method           | Description                                 |
|------------------|---------------------------------------------|
| `.keys()`        | Get all keys                                |
| `.values()`      | Get all values                              |
| `.items()`       | Get all key-value pairs                     |
| `.get(key)`      | Get value or None if key doesn't exist      |
| `.pop(key)`      | Remove and return the value for a key       |
| `.clear()`       | Remove all items from dictionary            |

---

## 🧪 Practice Exercises

### 🟢 Exercise 1: Create a Dictionary

Create a dictionary with your:
- name
- age
- favorite language

Print each item.

---

### 🔵 Exercise 2: Update the Age

Change the age, then print the updated dictionary.

---

### 🟠 Exercise 3: Loop Through

Loop through the dictionary and print:
```
name: Andrey
age: 25
language: Python
```

---

## ✅ Real-World Example

```python
users = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob": {"age": 25, "email": "bob@example.com"}
}

print(users["bob"]["email"])  # ➜ bob@example.com
```