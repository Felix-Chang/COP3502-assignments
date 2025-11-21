def reformat(data):
    new_data = {}
    for item in data:
        if new_data.get(item["type"], False):
            new_data[item["type"]][item["name"]] = item["price"]

        else:
            new_data[item["type"]] = {}
            new_data[item["type"]][item["name"]] = item["price"]

    return new_data

def nth(data, n):
    if n > 0:
        if data[1] is None:
            return None
        data = data[1]
    else:
        if not (data[n] is None):
            return data[0]
        else:
            return None

    n -= 1
    return nth(data, n)
    
def where(data):
    count = 0
    if type(data) == str:
        if data == "Waldo":
            count += 1
    elif type(data) == list:
        for elem in data:
            count += where(elem)
    elif type(data) == dict:
        for key, value in data.items():
            if key == "Waldo":
                count += 1
            count += where(value)
    return count

data = {
    "Waldo": [
        "Wilma",
        "Willy",
        "Walter",
        "Wendy",
        {
            "Will": "William",
            "Wren": ["Waldo", "Warren"],
        },
    ],
    "Wanda": {
        "Whitney": "Waldo",
        "Woody": ["Willard", "Webster", "Waldo"]
    },
    "Wilber": {
        "Waldo": "Wednesday",
        "Wade": "Wilson",
        "Wallace": ["Wilfred", "Waldo"]
    },
}
