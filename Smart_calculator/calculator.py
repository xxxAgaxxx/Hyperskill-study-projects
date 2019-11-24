def get_numbers():
    """Gets keyboard input, checks, that it is not /exit  command
    :return: True if input correct, False if /exit
    """
    input_line = input()
    if input_line == '/exit':
        return 0
    if input_line == '/help':
        print('The program calculates the sum of numbers')
        return 2
    if input_line == '':
        return 2
    expression_to_process[:] = input_line.split()
    return 1


def make_calculations(expression):
    # if len(numbers) == 0:
    #     return False
    result = int(expression[0])
    if len(expression) == 1:
        return result
    else:
        # 1. нужно итерировать с шагом 2 (срез или range(0,n,2))
        # 2. срез не подходит, т.к. в i будет элемент n, а как обратиться к n+1, если не знаешь номера?
        # 3. вариант с zip
        # iterable_expression = iter(expression)
        # for i, j in zip(iterable_expression, iterable_expression):
        for i in range(1, len(expression), 2):
            # odd number of - => subtraction
            if expression[i].count('-') % 2 == 1:
                result -= int(expression[i+1])
            else:
                result += int(expression[i+1])
        return result


expression_to_process = []
while True:
    operation_code = get_numbers()
    if operation_code == 1:
        operation_result = make_calculations(expression_to_process)
        print(operation_result)
        continue
    if operation_code == 2:
        continue
    if operation_code == 0:
        break
print('Bye!')
