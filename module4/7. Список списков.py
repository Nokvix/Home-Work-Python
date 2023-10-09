nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
result = [i_third_level for i_first_level in nice_list for i_second_level in i_first_level for i_third_level in
          i_second_level]
print(result)
