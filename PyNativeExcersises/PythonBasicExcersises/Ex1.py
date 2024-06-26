number1 = 20

number2 = 30


def productOrSum(number1, number2):

    number3 = int(number1) * int(number2)
    if number3 >= 1000:
        return print("the sum is : ", int(number1) + int(number2))
    else:
        return print(f"the product is :{number3}")


productOrSum(number1, number2)


number1 = 40
number2 = 30
productOrSum(number1, number2)