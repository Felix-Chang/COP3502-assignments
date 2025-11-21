def print_backwards(string):
    if string == "":
        return
    print(string[-1], end = "")
    print_backwards(string[:-1])

def format_names(name_list):
    if not name_list:
        return []
    if "," in name_list[0].split()[0]:
        new_name = [name_list[0]]
    else:
        new_name = [name_list[0].split()[1] + ", " + name_list[0].split()[0]]
    return new_name + format_names(name_list[1:])

def sum_a(dictionaries):
    if not dictionaries:
        return 0
    return dictionaries[0].get("a", 0) + sum_a(dictionaries[1:])
    
def process_list(numbers):
    evens = [str(numbers[i]) for i in range(0, len(numbers), 2)]
    odds = [numbers[i] * 10 for i in range(1, len(numbers), 2)]
    return evens + odds