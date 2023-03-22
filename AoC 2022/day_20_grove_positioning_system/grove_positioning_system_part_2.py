from input_parser import get_puzzle_input


class ListItem:
    previous_item = None
    next_item = None

    def __init__(self, id, value):
        self.value = value
        self.id = id

    def get_value(self):
        return self.value

    def get_id(self):
        return self.id

    def get_previous_item(self):
        return self.previous_item

    def get_next_item(self):
        return self.next_item

    def sort(self):

        if self.value > 0:
            for i in range(self.value % (len(gps_data)-1)):
                self.move_forward()

        elif self.value < 0:
            for i in range(abs(self.value) % (len(gps_data)-1)):
                self.move_backward()

    def move_forward(self):
        prev = self.get_previous_item()
        nxt = self.get_next_item()
        nxt_nxt = nxt.get_next_item()

        prev.next_item = nxt
        nxt.previous_item = prev

        nxt.next_item = self
        nxt_nxt.previous_item = self

        self.next_item = nxt_nxt
        self.previous_item = nxt

    def move_backward(self):
        prev = self.get_previous_item()
        nxt = self.get_next_item()
        prev_prev = prev.get_previous_item()
        nxt.previous_item = prev
        prev.next_item = nxt
        prev.previous_item = self
        prev_prev.next_item = self
        self.previous_item = prev_prev
        self.next_item = prev


class GPS:
    def __init__(self, first_item):
        self.first_item = first_item
        self.first_item.previous_item = self.first_item
        self.first_item.next_item = self.first_item

    def find_item_with_id(self, id):
        item = self.first_item
        while item.get_id() != id:
            item = item.get_next_item()
            if item.get_id() == self.first_item:
                return False
        return item

    def find_item_at_position(self, position):
        item = self.first_item
        for i in range(position):
            item = item.get_next_item()
        return item

    def sort_item(self, id):
        item = self.find_item_with_id(id)
        item.sort()

    def print_list(self):
        item = self.first_item
        while True:
            print(item.get_value())
            item = item.get_next_item()
            if item.get_id() == self.first_item.get_id():
                break

    def append_item(self, item):
        prev = self.first_item.get_previous_item()
        prev.next_item = item
        self.first_item.previous_item = item

        item.next_item = self.first_item
        item.previous_item = prev


gps_data = get_puzzle_input('input.txt')

gps = None
pre_zero_items = []

decryption_key = 811589153

for i in range(len(gps_data)):
    new_list_item = ListItem(i, int(gps_data[i])*decryption_key)

    if gps_data[i] == '0':
        gps = GPS(new_list_item)

    elif gps == None:
        pre_zero_items.append(new_list_item)
    else:
        gps.append_item(new_list_item)

for item in pre_zero_items:
    gps.append_item(item)

# gps.print_list()


for h in range(10):
    for i in range(len(gps_data)):
        gps.sort_item(i)
    # print('\n\n')
    # gps.print_list()


testing_numbers = [1000, 2000, 3000]
coordinate_sum = 0

for number in testing_numbers:
    coordinate = gps.find_item_at_position(number)
    coordinate_sum += coordinate.get_value()
    print('The '+str(number)+'th number after 0 is '+str(coordinate.get_value()))

print('the sum of coordinates is: '+str(coordinate_sum))
