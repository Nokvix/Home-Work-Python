def expand_lists(processing_list):
    result = []
    for i_elem in processing_list:
        if not isinstance(i_elem, list):
            result.append(i_elem)
        else:
            result.extend(expand_lists(i_elem))
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
expanded_list = expand_lists(nice_list)
print(expanded_list)
