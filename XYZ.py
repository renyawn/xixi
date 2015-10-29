
import random
import time

def init_winner_log(how_many_player):

    winner_log_dict = {}
    
    for i in range(how_many_player):
        winner_log_dict[i] = 0

    return winner_log_dict



def which_two_flag(list_item):

    item_set = set()
    except_num = 0

    for i in list_item:
        if i != except_num:
            item_set.add(i)

    return tuple(item_set)


def return_win_flag(item1, item2):
    '''input: 1 or 2 or 3'''
    max_num = max(item1, item2)
    min_num = min(item1, item2)

    diff = max_num - min_num

    if diff == 1:
        return max_num 
    if diff == 2:
        return min_num

def return_lose_flag(item1, item2):
    '''input: 1 or 2 or 3'''
    max_num = max(item1, item2)
    min_num = min(item1, item2)

    diff = max_num - min_num

    if diff == 1:
        return min_num
    if diff == 2:
        return max_num

def is_two_kind(list_item):
    '''like:[0, 1, 2, 3, 1, 1, ..., ...]'''
    init_set = set()
    except_num = 0

    for i in list_item:
        if i != except_num:
            init_set.add(i)

    if len(init_set) == 2:
        return True
    else:
        return False

def make_out_game(list_item, lose_num):

    out_flag = 0

    while list_item.count(lose_num):
        list_item[(list_item.index(lose_num))] = out_flag

def init_flag_list(how_many_player):

    flag_list = []
    choice_list = [1, 2, 3]
    
    for i in range(how_many_player):
        flag_list.append(random.choice(choice_list))

    return flag_list
        
def is_only_one_winner(list_item, how_many_player):

    out_flag = 0
    return list_item.count(out_flag) == (how_many_player - 1)

def index_of_winner(list_item):
    
    out_flag = 0
    for i in list_item:
        if i != out_flag:
            return list_item.index(i)

def make_new_flag(list_item):

    out_flag = 0
    choice_list = [1, 2, 3]
    for i, j in enumerate(list_item):
        if j != out_flag:
            list_item[i] = random.choice([1, 2, 3])

def nice_list(list_item):

    map_dict = {
        1: 'Y',
        2: 'E',
        3: 'U',
        0: '_'
    }

    nice_str = ''

    for i in list_item:
        nice_str += map_dict[i]

    return nice_str

# def nice_dict(dict_item, how_many_winner):

#     nice_str = ''
    
#     for i in range(len(dict_item)):

#         nice_str += 'player' + str(i) + ':\t' + str(dict_item[i]) + +'\n' 

#     return nice_str



def guess_game(how_many_player, how_many_winner):

    winner_counter = 0
    winner_log = init_winner_log(how_many_player)

    while winner_counter < how_many_winner:



        flag_list = init_flag_list(how_many_player)
        # print(nice_list(flag_list))

        while True:

            if is_two_kind(flag_list):
                
                flag1, flag2 = which_two_flag(flag_list)
                win_flag = return_win_flag(flag1, flag2)
                lose_flag = return_lose_flag(flag1, flag2)

                make_out_game(flag_list, lose_flag)

                if is_only_one_winner(flag_list, how_many_player):

                    winner_index = index_of_winner(flag_list)
                    winner_log[winner_index] += 1
                    winner_counter += 1
                    # print('[' + nice_list(flag_list) + ']')
                    break

                else:
                    make_new_flag(flag_list)
                    # print(nice_list(flag_list))

                    continue
            else:
                make_new_flag(flag_list)
                # print(nice_list(flag_list))

    # print(nice_dict(winner_log))

guess_game(20, 10)
