
OUT_OF_BOUNDS = float('-inf')
# print(OUT_OF _BOUNDS)
def calculate(first_number, second_number, operator):
    result = 0
    if operator == "+":
        result = first_number + second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    elif operator == "-":
        result = first_number - second_number
    else:
       result = OUT_OF_BOUNDS

    return result
first_number = input("What is the first number? ")
first_number = int(first_number)

second_number = input("What is the second number? ")
second_number = int(second_number)

operator = input("What operation do you want me to do (+, -, *, /,)?")
operator = operator.strip()

result = calculate (first_number, second_number, operator)

if result == OUT_OF_BOUNDS:
    print("you need a valid operator (+, -, *, /)")
else:
    print(result)
