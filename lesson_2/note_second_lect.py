import math
import sys

def index_to_bytes(value, bits):
    n = bits // 8
    if bits % 8 != 0:
        n += 1
    return value.to_bytes(n, 'little')


if not (2 <= len(sys.argv) <= 3):
    print('Usage: python3', sys.argv[0], 'input_file (output_file)')
    exit(-1)

# r - raw (строка воспринимается буквально как строка без спец. символов)
# path = r'/home/ksusha/narnia/iscra/python/ISCRA-s2023-python/lesson_2/note_second_lect.py'

with open(sys.argv[1], 'rb') as file:
    data = file.read()

# # вывод каждого байта
# for sym in data:
    # print(hex(sym))
#
# # вывод содержимого файла
# print(data.decode('utf-8'))

# кортеж из одного элемента
dictionary = {(i,): i for i in range(256)}
sequence = list()

outpath = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1] + '.lzw'
with open(outpath, 'wb') as file:
    for sym in data:
        sequence.append(sym)
        key = tuple(sequence)
        if key in dictionary:
            continue
        print(key)
        n = math.ceil(math.log2(len(dictionary)))
        print(n)
        # поиск по key, но без последнего элемента
        index_value = dictionary[key[:-1]] # получаем код из словаря
        print(index_value)
        enc_value = index_to_bytes(index_value, n)
        print(enc_value)
        file.write(enc_value)

        value = len(dictionary)
        dictionary[key] = value

        # список только из последнего элемента
        sequence = sequence[-1:]

    n = math.ceil(math.log2(len(dictionary)))
    index_value = dictionary[tuple(sequence)]
    enc_value = index_to_bytes(index_value, n)
    file.write(enc_value)
    print(dictionary)
# print(dictionary)

