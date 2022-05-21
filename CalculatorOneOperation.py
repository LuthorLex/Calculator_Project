# Single Operation Calculator

def requestOperator():

    while True:

        operator = input('Enter Operator: ')

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


operations = ['+', '/', '-', '*', '^']

print('+ -> Addition\n- -> Subtraction\n* -> Multiplication\n/ -> Division\n^ -> Power')

operator = requestOperator()
x = requestValue()
y = requestValue()

result = operation(x, y, operator)

print('Result is ', result)
