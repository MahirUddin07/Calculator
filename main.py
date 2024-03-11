def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def upp(num1, num2):
    return num1 ** num2

run = True
while run:
    user_inp = input('Kör? : ')
    if user_inp == 'nej':
        run = False
    else:
        num1 = float(input('Choose first number: '))
        num2 = float(input('Choose second number: '))

        print('choose operation: ')
        print('1. add')
        print('2. sub')
        print('3. mult')
        print('4. div')
        choose = input('choose operation: ')

        if choose == '1':
            result_add = add(num1, num2)
            print(result_add)
        elif choose == '2':
            result_sub = sub(num1, num2)
            print(result_sub)
        elif choose == '3':
            result_mult = mult(num1, num2)
            print(result_mult)

        elif choose == '4':
            result_div = div(num1, num2)
            print(result_div)