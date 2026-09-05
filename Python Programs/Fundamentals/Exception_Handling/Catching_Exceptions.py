# Error - Issues in the program logic like syntax error which occurs at a compile time.
# Exception - Problems that occur at a run-time and can be managed using execption handling.

# 1. Specific exceptions
try:
    # value error
    x = int("Str")
    inv = 1/x

except ValueError:
    print("Not valid")

except ZeroDivisionError:
    print("Zero has no inverse")

# 2. Multiple exceptions

a=["19","twenty",30]
try:
    # string cant be converted into int
    total = int(a[0])+int(a[1])

except (ValueError, TypeError) as e:
    print("Error: ", e)

except IndexError:
    print("Index out of range")

finally:
    print(total)

# 3. Catch-all

try:
    res="100"/20
except ArithmeticError:
    print("Arithmetic problem")
except:
    print("Something wrong")