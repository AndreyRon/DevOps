
# 🛡️ Python `try` / `except` / `finally` Summary

## 🔹 `try`
Used to **run code that might raise an error**.

```python
try:
    risky_code()
```

## 🔹 `except`
Used to **catch and handle** specific errors.

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number!")
```

## 🔹 Multiple `except`s
Handle different error types separately.

```python
try:
    print(10 / int(input("Enter number: ")))
except ValueError:
    print("You didn't enter a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

## 🔹 `finally`
Code that **runs no matter what**, even if an error happens.

```python
try:
    f = open("file.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Cleanup done.")
```

---

## ✅ Best Practices
- Catch **specific** exceptions (not just `except:`)
- Use `finally` for cleanup (e.g. close files, release resources)