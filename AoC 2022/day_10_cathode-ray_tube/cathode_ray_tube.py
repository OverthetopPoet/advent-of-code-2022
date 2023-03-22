from input_parser import get_puzzle_input


class CPU:
    def __init__(self, cycles_of_interest=[]):
        self.cycles_of_interest = cycles_of_interest
        self.cycle = 1
        self.register = 1
        self.signal_strength = 0
        self.crt = []
        self.sprite = [0, 1, 2]
        self.crt_row = -1

    def get_signal_strength(self):
        self.calculate_cycle_signal_strenght()
        return self.signal_strength

    def noop(self):
        #print('Start of noop. Cycle= '+str(self.cycle)+' Register= '+str(self.register))
        self.calculate_cycle_signal_strenght()
        self.set_pixel()
        self.cycle += 1
        #print('End of noop. Cycle= '+str(self.cycle)+' Register= '+str(self.register))

    def addx(self, v):
        #print('Start of addx('+str(v)+'). Cycle= '+str(self.cycle)+' Register= '+str(self.register))
        completion_cycles = 2

        for i in range(completion_cycles):
            #print('Cycle '+str(i+1)+' of addx('+str(v)+'). Cycle= '+str(self.cycle)+' Register= '+str(self.register))
            self.calculate_cycle_signal_strenght()
            self.set_pixel()
            self.cycle += 1

        self.register += v
        self.sprite = [self.register-1, self.register, self.register+1]
        #print('End of addx('+str(v)+'). Cycle= '+str(self.cycle)+' Register= '+str(self.register))

    def parse_input(self, input):
        if input == 'noop':
            self.noop()
        else:
            self.addx(int(input.split(' ')[1]))

    def calculate_cycle_signal_strenght(self):
        if self.cycles_of_interest != []:
            cycle_strength = self.cycle*self.register
            if self.cycle in self.cycles_of_interest:
                self.signal_strength += cycle_strength

    def set_pixel(self):
        crt_position = int(self.cycle % 40)-1
        if crt_position == 0:
            self.crt_row += 1
            self.crt.append([])

        if crt_position in self.sprite:
            self.crt[self.crt_row].append('#')
        else:
            self.crt[self.crt_row].append('.')

    def draw_crt(self):
        for row in self.crt:
            crt_row = ''
            for pixel in row:
                crt_row += pixel
            print(crt_row)


cpu_instructions = get_puzzle_input('input.txt')

cycles_of_interest = [20, 60, 100, 140, 180, 220]
cpu = CPU(cycles_of_interest)
for instruction in cpu_instructions:
    cpu.parse_input(instruction)

signal_strenght = cpu.get_signal_strength()

print('the signal strenth of the CPU is: '+str(signal_strenght))

cpu.draw_crt()
