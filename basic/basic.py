def salary_calc():
    option = 1

    while option:
        salary = input('Enter salary: ')
        tax    = input('Enter Tax: ')
        print(calc(salary, tax))

        option = input('Enter zero for exit: ')

def calc(salary, tax = 10):
    return salary - salary * (tax * 0.01)

def simple_calc():
    number1 = input('Enter number one: ')
    operator = input('Enter operator: ')
    number2 = input('Enter number two: ')
    result = None
    message = 'Result is: '

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '/':
        result = float(number1) / float(number2)
    elif operator == '*':
        result = number1 * number2
    else:
        return 'Operator not found'

    message += str(round(result, 2))
    return message

if __name__ == '__main__':
    # print(simple_calc())
    salary_calc()