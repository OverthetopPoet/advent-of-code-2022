from input_parser import get_puzzle_input

def get_monkey_result(monkey_name):
    monkey=monkeys[monkey_name]

    if monkey_name=='root':
        operand1=get_monkey_result(monkey['operation']['operand1'])
        operand2=get_monkey_result(monkey['operation']['operand2'])
        return operand1==operand2

    if monkey['result']!=None:
        return monkey['result']

    else:
        operand1=get_monkey_result(monkey['operation']['operand1'])
        operand2=get_monkey_result(monkey['operation']['operand2'])
        operation=monkey['operation']['operation']
        return solve_monkey_math(operand1,operand2,operation)

def get_monkey_equation(monkey_name):
    monkey=monkeys[monkey_name]

    if monkey_name=='root':
        operand1=get_monkey_equation(monkey['operation']['operand1'])
        operand2=get_monkey_equation(monkey['operation']['operand2'])
        return str(operand1)+'='+str(operand2)
    
    if monkey_name=='humn':
        return monkey_name

    if monkey['result']!=None:
        return monkey['result']

    else:
        operand1=get_monkey_equation(monkey['operation']['operand1'])
        operand2=get_monkey_equation(monkey['operation']['operand2'])
        operation=monkey['operation']['operation']

        if str(operand1).isnumeric() and str(operand2).isnumeric():
            return solve_monkey_math(int(operand1),int(operand2),operation)
        else:
            return '(' +str(operand1)+' '+operation+' '+str(operand2)+')'
            
        

def solve_monkey_math(operand1,operand2,operation, reverse=False):
    if reverse:
        if operation=='+':
            operation='-'
        elif operation=='-':
            operation='+'
        elif operation=='*':
            operation='/'
        elif operation=='/':
            operation='*'

    if operation=='+':
        return operand1+operand2
    if operation=='-':
        return operand1-operand2
    if operation=='*':
        return operand1*operand2
    if operation=='/':
        result=operand1/operand2
        #print(result,operand1,operand2)
        return int(result)

def brute_force_solver():
    own_name='humn'
    own_number=-1
    while True:
        own_number+=1
        monkeys.update({own_name:{'result':own_number,'operation':{'operand1':None,'operation':None,'operand2':None}}})
        if get_monkey_result('root'):
            break
        own_number*=-1
        monkeys.update({own_name:{'result':own_number,'operation':{'operand1':None,'operation':None,'operand2':None}}})
        if get_monkey_result('root'):
            break
        own_number*=-1

def solve_equation(equation):
    solution=int(equation.split('=')[1])
    to_be_solved=equation.split('=')[0][1:-1]

    if '(' not in to_be_solved:
        return equation

    in_brackets=to_be_solved
    standalone=to_be_solved
    standalone_front=False

    if to_be_solved.startswith('('):
        while not in_brackets.endswith(')'):
            in_brackets=in_brackets[:-1]
        while ')' in standalone:
            standalone=standalone[1:]

    elif to_be_solved.endswith(')'):
        standalone_front=True
        while not in_brackets.startswith('('):
            in_brackets=in_brackets[1:]
        while '(' in standalone:
            standalone=standalone[:-1]

    if standalone.endswith(' '):
        standalone=standalone[:-1]
    if standalone.startswith(' '):
        standalone=standalone[1:]
    split_standalone=standalone.split(' ')

    operation=None
    operand=None

    if standalone_front:
        operation=split_standalone[1]
        operand=int(split_standalone[0])
        if operation=='/' or operation == '-':
            solution=solve_monkey_math(operand, solution, operation)
        else:
            solution=solve_monkey_math(solution,operand,operation,True)

    else:
        operation=split_standalone[0]
        operand=int(split_standalone[1])
        solution=solve_monkey_math(solution,operand,operation,True)
    new_equation=solve_equation(in_brackets+'='+str(solution))
    return new_equation
    

    




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

#brute force approach
#own_number=brute_force_solver()

#for monkey in monkeys:
#    print(monkeys[monkey])

monkey_equation=get_monkey_equation('root')
print(monkey_equation)

monkey_equation=solve_equation(monkey_equation)
print(monkey_equation)
monkey_equation=monkey_equation.replace(' ','')
monkey_equation=monkey_equation.replace('(','')
monkey_equation=monkey_equation.replace(')','')

print('I yell the number: '+str(int(monkey_equation.split('=')[1])+int(monkey_equation.split('=')[0].split('-')[1])))


