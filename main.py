import re

array1 = []
array2 = []

def create_array(pair, array):
    for item in range(int(pair[0]), int(pair[1])+1):
        array.append(item)

def process_line(line):
    pair = re.split('\n|,', line)
    first = re.split('-', pair[0])
    second = re.split('-', pair[1])
    create_array(first, array1)
    create_array(second, array2)
    if set(array1).intersection(set(array2)) or set(array2).intersection(set(array1)):
        return True
    return False

numLines = 0
with open('input.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        if process_line(line) == True:
            print("It contains!")
            numLines += 1
        line = reader.readline()
        array1.clear()
        array2.clear()
    print(numLines)


