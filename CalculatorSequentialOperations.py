# Calculator with subsquent operations

def requestOperator():

    while True:

        operator = input('Enter Operation: ')

        if operator in operations:
            return operator
        else:
            print('Invalid operation')


def requestValue():

    while True:

        number = input('Enter a number: ')

        try:
            return float(number)
        except:
            print('Invalid number, Again please')


def operation(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '/':
        return x / y
    elif operator == '*':
        return x * y
    elif operator == '^':
        return x ** y


operations = ['+', '/', '-', '*', '^', 'done']

print('+ -> Addition\n- -> Subtraction\n* -> Multiplication\n/ -> Division\n^ -> Power\nClose -> done')

while True:     # 1st Round

    operator = requestOperator()
    if operator == 'done':
        print('Module Shutdown')
        quit()
    x = requestValue()
    y = requestValue()

    result = operation(x, y, operator)

    print('Result is ', result)

    while True:  # Subsq Ronds
        operator = requestOperator()

        if operator == 'done':
            print('Module Shutdown')
            quit()
        else:
            y = requestValue()

            result = operation(result, y, operator)
            print('Result is ', result)

# Must attempt with single while loop
