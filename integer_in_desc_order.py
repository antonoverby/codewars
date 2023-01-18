def descending_order(num):
    num_str = [i for i in str(num)]
    new_list = []
    for i in num_str:
        new_list.append(int(i))
        new_list.sort(reverse=True)
    final_list = []
    for i in new_list:
        final_list.append(str(i))
    result = ''.join(final_list)
    return int(result)
    
descending_order(123)