from random import sample
from math import inf

def split(array: list, stack_size: int):
    split_array = []
    for i in range(0, len(array), stack_size):
        split_array.append(array[i:i+stack_size])
    return split_array

def order(array: list, time: int):
    array.sort()
    length = len(array)
    time += ((length)(length + 1)) / 2
    return array, time

def collate(array1: list, array2: list, time: int):
    array = []
    for value in array1:
        array.append(value)
    for value in array2:
        array.append(value)
    time += len(array) * 2 + 1
    array.sort()
    return array, time

deck = [i for i in range(1,1025)]
min_time = inf

for m in range(10, 0, -1):
    unordered_deck = sample(deck, 1024)
    time = 1000
    stack_count = 2 ** m
    unordered_deck = split(unordered_deck, stack_count)
    while unordered_deck != deck and len(unordered_deck) < 1024:
        for i in range(0, len(unordered_deck)-1):
            try:
                # Collate two sections of equal length into one
                collated, time = collate(unordered_deck[i], unordered_deck[i+1], time)
            except IndexError as e:
                print(i)
                print(len(unordered_deck))
                raise e
            if time > min_time:
                break
        print(f"{time/100:.2f} {m}")
    print(int(time) * 0.017)
    if time < min_time:
        min_time = time
        min_stack_size = stack_count 