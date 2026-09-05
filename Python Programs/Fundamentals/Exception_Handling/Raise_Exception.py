def set(age):
    if age < 0:
        raise ValueError("Age cant be negative")
    print(f'Age set to {age}')

try:
    set(-5)
except ValueError as e:
    print(e)