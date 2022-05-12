def greeting(greeting, name):
    print(f"{greeting}! {name}")


def sum(number1, number2, number3):
    return int(number1)  + int(number2) + int(number3)


def percent(value, percent):
    return value + (value * percent)


def fizz_buzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "fizzBuzz"
    
    if value % 3 == 0:
        return "fizz"

    if value % 5 == 0:
        return "buzz"
    
    return value

for i in range(10):
    print(fizz_buzz(i))