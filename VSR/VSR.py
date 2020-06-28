'''
 1.3 Создание программы для считывания данных формата CSV с использованием функционала модуля contextlib.
'''

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()


with open_file('VSR.csv', 'r') as file:
    for line in file:
        new_line = line.split(';')
        new_line[-1] = new_line[-1].split('\n')
        print("%10s%10s" % (new_line[0], new_line[-1][0]))
