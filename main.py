# import math
#
# my_list = [1, 2, 3, 4, 5, 6]
# first_list = my_list[0:3]
# second_list = my_list[3:6]
# print([first_list, second_list])
#
# my_list = [1, 2, 3]
# first_list = my_list[0:2]
# second_list = my_list[2:]
# print([first_list, second_list])
#
# my_list = [1, 2, 3, 4, 5]
# first_list = my_list[0:3]
# second_list = my_list[3:5]
# print([first_list, second_list])
#
# my_list = [1]
# first_list = my_list[0:]
# second_list = my_list[1:]
# print([first_list, second_list])
#
# my_list = []
# first_list = my_list[0:]
# second_list = my_list[1:]
# print([first_list, second_list])

def separate_list(listik):
    mid = (len(listik) + 1) // 2
    first_lst = listik[:mid]
    second_lst = listik[mid:]
    return [first_lst, second_lst]

my_list = []
result = separate_list(my_list)
print(result)



