

def calculator():
    if(operand == '+'):
        return number1 + number2
    elif(operand == '*'):
        return number1 * number2
    elif(operand == '/'):
        return number1 / number2
    elif(operand == '-'):
        return number1 - number2
    else:
        print('Enter correct operand')

while True:
    try:
        number1 = int(input("Enter first number: "))
        operand = input('Enter operand (+, *, /, -): ')
        number2 = int(input("Enter second number: "))
        choice = input('Press q to quit the program or enter to contunie: ')

        if (choice == 'q'):

            break

        else:
            print(calculator())

    except ValueError:
        print('Enter a valid number')
