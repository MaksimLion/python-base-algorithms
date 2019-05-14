def selection_sort(sort_list):
    sorted_list = list()
    for i in range(len(sort_list)):
        min_value_index = sort_list.index(min(sort_list))
        sorted_list.append(sort_list.pop(min_value_index))
    return sorted_list
    