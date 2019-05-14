import random
from time_tracker import time_checker


@time_checker
def binary_search(sorted_list, item):
    left_border = 0
    right_border = len(sorted_list)
    while left_border <= right_border:
        middle_value = (left_border + right_border) // 2
        if sorted_list[middle_value] == item:
            return middle_value
        if sorted_list[middle_value] > item:
            right_border = middle_value
        else:
            left_border = middle_value

