from input_parser import get_puzzle_input


class Monkey:
    def __init__(self, name, starting_items, operation_sign, operand, test_value, true_test_monkey, false_test_monkey):
        self.name = name
        self.item_list = starting_items
        self.operation_sign = operation_sign
        self.operand = operand
        self.test_value = test_value
        self.true_test_monkey = true_test_monkey
        self.false_test_monkey = false_test_monkey
        self.monkey_business = 0
        self.monkey_list = []

    def inspect(self, worry_level):
        operand = self.operand
        if self.operand == 'old':
            operand = worry_level
        if self.operation_sign == '+':
            worry_level += operand
        elif self.operation_sign == '*':
            worry_level *= operand

        return worry_level

    def relief(self, worry_level):
        return int(worry_level/3)

    def throw(self):
        worry_level = self.item_list[0]
        self.item_list.pop(0)
        if worry_level % self.test_value == 0:
            self.monkey_list[self.true_test_monkey].receive_item(worry_level)
        else:
            self.monkey_list[self.false_test_monkey].receive_item(worry_level)

    def set_monkey_list(self, monkey_list):
        self.monkey_list = monkey_list

    def receive_item(self, worry_level):
        self.item_list.append(worry_level)

    def take_turn(self):
        nr_items = len(self.item_list)
        for i in range(nr_items):
            self.item_list[0] = self.inspect(self.item_list[0])
            self.item_list[0] = self.relief(self.item_list[0])
            self.throw()
            self.monkey_business += 1

    def get_monkey_business(self):
        return self.monkey_business

    def get_name(self):
        return self.name


monkey_list = []
starting_items = []
operation_sign = ''
operand = 0
test_value = 0
true_test_monkey = 0
false_test_monkey = 0
monkey_nr = 0


monkey_descriptions = get_puzzle_input('input.txt')
nr_turns = 20

for line in monkey_descriptions:
    if 'Starting items' in line:
        line = line.replace(' ', '')
        while ':' in line:
            line = line[1:]
        if ',' in line:
            split_line = line.split(',')
            starting_items = []
            for item in split_line:
                starting_items.append(int(item))
        else:
            starting_items = [int(line)]
    elif 'Operation' in line:
        while '=' in line:
            line = line[1:]
        line = line[1:]
        split_line = line.split(' ')
        operation_sign = split_line[1]
        if split_line[2] == 'old':
            operand = 'old'
        else:
            operand = int(split_line[2])

    elif 'Test' in line:
        while ' ' in line:
            line = line[1:]
        test_value = int(line)
    elif 'true' in line:
        while ' ' in line:
            line = line[1:]
        true_test_monkey = int(line)
    elif 'false' in line:
        while ' ' in line:
            line = line[1:]
        false_test_monkey = int(line)

        new_monkey = Monkey('Monkey '+str(monkey_nr), starting_items, operation_sign,
                            operand, test_value, true_test_monkey, false_test_monkey)
        starting_items = []
        operation_sign = ''
        operand = 0
        test_value = 0
        true_test_monkey = 0
        false_test_monkey = 0
        monkey_nr += 1
        monkey_list.append(new_monkey)


for monkey in monkey_list:
    monkey.set_monkey_list(monkey_list)

for i in range(nr_turns):
    for monkey in monkey_list:
        print(monkey.get_name()+'s turn nr '+str(i))
        monkey.take_turn()

monkey_business_list = []

for monkey in monkey_list:
    print(monkey.get_name()+' inspected items '+str(monkey.get_monkey_business())+' times.')
    monkey_business_list.append(monkey.get_monkey_business())

monkey_business_list.sort()
monkey_business_level = monkey_business_list[len(monkey_business_list)-1] * \
    monkey_business_list[len(monkey_business_list)-2]

print('The overall monkey business level is: '+str(monkey_business_level))
