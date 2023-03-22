from input_parser import get_puzzle_input
import json


def lists_in_order(list_1, list_2):
    # wenn rückgabewert einmal 2 ist muss er das auch bleiben und direkt 2 returned werden

    smallest_range = min([len(list_1), len(list_2)])

    for i in range(smallest_range):
        if type(list_1[i]) == int and type(list_2[i]) == int:
            if list_1[i] > list_2[i]:
                return 0
            elif list_1[i] < list_2[i]:
                return 2
        elif type(list_1[i]) == list and type(list_2[i]) == list:
            list_in_order = lists_in_order(list_1[i], list_2[i])
            if list_in_order == 0:
                return 0
            elif list_in_order == 2:
                return 2
        else:
            new_list_1 = []
            new_list_2 = []
            if type(list_1[i]) == int:
                new_list_1 = [list_1[i]]
                new_list_2 = list_2[i]
            elif type(list_2[i]) == int:
                new_list_1 = list_1[i]
                new_list_2 = [list_2[i]]
            list_in_order = lists_in_order(new_list_1, new_list_2)
            if list_in_order == 0:
                return 0
            elif list_in_order == 2:
                return 2

    if len(list_1) > len(list_2):
        return 0
    elif len(list_1) < len(list_2):
        return 2
    else:
        return 1


signal_list = get_puzzle_input('input.txt')

signal_pairs = []

new_pair = []

for signal in signal_list:
    if signal == '':
        signal_pairs.append(new_pair)
        new_pair = []

    else:
        translated_signal = json.loads(signal)
        new_pair.append(translated_signal)

correct_pair_sum = 0
for i in range(len(signal_pairs)):
    if lists_in_order(signal_pairs[i][0], signal_pairs[i][1]) != 0:
        correct_pair_sum = correct_pair_sum + i+1

print('The index sum of correct pairs is: '+str(correct_pair_sum))
