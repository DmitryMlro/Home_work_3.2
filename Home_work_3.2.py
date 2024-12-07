# [12, 3, 4, 10]
my_list = [12, 3, 4, 10]
result_1 = my_list[-1:] + my_list[:-1]
print(my_list, "=>", result_1)

# [1] => [1]
my_list_2 = [1]
result_2 = my_list_2[-1:] + my_list_2[:-1]
print(my_list_2, "=>", result_2)

# [] => []
my_list_3 = []
result_3 = my_list_3[-1:] + my_list_3[:-1]
print(my_list_3, "=>", result_3)

# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
my_list_4 = [12, 3, 4, 10, 8]
result_4 = my_list_4[-1:] + my_list_4[:-1]
print(my_list_4, "=>", result_4)