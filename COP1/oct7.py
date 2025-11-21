numbers = [5,5,4,8,5,1,5]

def remove_all(my_list, value):

    for i in range(len(my_list)-1, -1, -1):
        if my_list[i] == value:
            my_list.pop(i)

    return my_list

print(remove_all(numbers, 5))