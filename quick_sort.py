
def quick_sort(number_list):
    """
    Quick sort algorithm.

    :param number_list: a number list for sorting
    :return: a sorted number list
    """
    
    if len(number_list) <= 1:
        return number_list
    
    left_list = []
    right_list = []
    pivot = number_list[0]

    for item in number_list[1:]:
        if item <= pivot:
            left_list.append(item)
        else:
            right_list.append(item)

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


if __name__ == '__main__':
    number_list = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    print(quick_sort(number_list))

    
