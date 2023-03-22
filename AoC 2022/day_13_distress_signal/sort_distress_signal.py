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


def sort_signals(signals):
    for i in range(len(signals)-1):
        for j in range(len(signals)-1):
            if lists_in_order(signals[j],signals[j+1]) == 0:
                temp = signals[j]
                signals.pop(j)
                signals.insert(j+1,temp)
    return signals




signal_list = get_puzzle_input('input.txt')

signals= []
divider_packets=[[[2]], [[6]]]
for signal in signal_list:
    if signal!= '':
        translated_signal = json.loads(signal)
        if translated_signal in divider_packets:
            print('whoopsie')
        signals.append(translated_signal)


signals.extend(divider_packets)
sorted_signals=sort_signals(signals)
decoder_key = (sorted_signals.index(divider_packets[0])+1)*(sorted_signals.index(divider_packets[1])+1)

print('The decoder key is: '+str(decoder_key))
