# В этом файле необходимо реализовать функции task1() ... task10()
# НИЧЕГО НЕ УДАЛЯТЬ
def task1():
   num = int(input())
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def task2():
    age = int(input())
    if age < 18:
        print("Minor")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")
def task3():
    a = float(input())
    op = input().strip()
    b = float(input())
    match op:
        case '+':
            print(a + b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            print(a / b)
def task4():
    a = int(input())
    b = int(input())
    c = int(input())
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    print(maximum)
def task5():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not leap year")
def task6():
  temp = int(input())
    if temp < 0:
        print("Freezing")
    elif temp <= 20:
        print("Cool")
    elif temp <= 30:
        print("Warm")
    else:
        print("Hot")
def task7():
    score = int(input())
    if 90 <= score <= 100:
        print("A")
    elif 75 <= score <= 89:
        print("B")
    elif 60 <= score <= 74:
        print("C")
    elif 40 <= score <= 59:
        print("D")
    else:
        print("F")
def task8():
    day = int(input())
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
def task9():
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and a + c > b and b + c > a:
        print("Triangle exists")
    else:
        print("Triangle does not exist")
def task10():
    password = input()
    length = len(password)
    if length < 8:
        print("Weak")
    else:
        has_digit = any(ch.isdigit() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        if has_digit and has_upper:
            print("Strong")
        elif has_digit:
            print("Medium")
        else:
            print("Medium")


if __name__ == "__main__":
    pass
