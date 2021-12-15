def fizzbuzz():
    import math
    # nhap vao hai so bat ki xong split va chuyen thanh int
    numbers = input("Enter two numbers:")
    numbers = numbers.split(",")
    number1 = int(numbers[0])
    number2 = int(numbers[1])

    # Check so dau va so cuoi:
    if number1 > number2:
        print("Final number is smaller than first number")
    else:
        print("Get start")

    # chay vong lap fizz, buzz
    for i in range(number1, number2+1):
        if i % 3 == 0:
            print(i, ":fizz")
        elif i % 5 == 0:
            print(i, ":buzz")
        elif (i % 5 == 0) and (i % 3 == 0):
            print(i, ":fizzbuzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz()
