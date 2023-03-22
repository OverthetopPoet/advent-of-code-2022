from input_parser import get_puzzle_input

def get_monkey_result(monkey_name):
    monkey=monkeys[monkey_name]

    if monkey['result']!=None:
        return monkey['result']

    else:
        operand1=get_monkey_result(monkey['operation']['operand1'])
        operand2=get_monkey_result(monkey['operation']['operand2'])
        operation=monkey['operation']['operation']
        return solve_monkey_math(operand1,operand2,operation)

def solve_monkey_math(operand1,operand2,operation):
    if operation=='+':
        return operand1+operand2
    if operation=='-':
        return operand1-operand2
    if operation=='*':
        return operand1*operand2
    if operation=='/':
        result=operand1/operand2
        print(result,operand1,operand2)
        return result


monkey_screams=get_puzzle_input('input.txt')

monkeys={}

for monkey in monkey_screams:
    monkey_name=monkey.split(':')[0]
    monkey=monkey[6:]
    monkey_result=None
    operand1=None
    operation=None
    operand2=None

    if monkey.isnumeric():
        monkey_result=int(monkey)
    else:
        split_monkey=monkey.split(' ')
        operand1=split_monkey[0]
        operation=split_monkey[1]
        operand2=split_monkey[2]



    monkeys.update({monkey_name:{'result':monkey_result,'operation':{'operand1':operand1,'operation':operation,'operand2':operand2}}})

for monkey in monkeys:
    print(monkey,monkeys[monkey])

print(get_monkey_result('root'))

