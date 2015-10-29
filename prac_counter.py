#!/usr/bin/python3
import random
import time

def generate_num(max_dight):
    
    part_int = random.random()*10**max_dight
    part_float = random.random()*100 // 1 / 100
    
    return part_int + part_float

def prac_counter(line_times, max_dight):

    line_times = int(line_times)
    max_dight = int(max_dight)
    _count = 0
    _inter = 0.01

    for i in range(line_times):
        
        random_num = generate_num(max_dight)
        print('['+str(i)+']', '\t', random_num)
        _count += random_num

        time.sleep(_inter)

    _nice_count = _count*100 // 1 / 100
    print('---*---*---*---*---')
    print('[count]', '\t', _nice_count)

if __name__ == '__main__' :
    import sys
    prac_counter(*sys.argv[1:])
    
