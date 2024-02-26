my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [8, 9, 17, 16, 0],
]


outer_index = 0

while outer_index < len(my_list):
    inner_index = 0

    while inner_index < len(my_list[outer_index]):
        if my_list[outer_index][inner_index] % 2 == 0:
            print(my_list[outer_index][inner_index])
        inner_index += 1

    outer_index += 1
    
