def parse_student(info):
    student_info = info.split()
    student_dict = {}
    student_dict["id"] = int(student_info[0][0:8])
    student_dict["name"] = student_info[0][8:] + " " + student_info[1][:-4]
    student_dict["birthdate"] = student_info[1][-4:-2] + "/" + student_info[1][-2:]

    return student_dict

def count_items(item_list):
    dc = {}
    for item in item_list:
        dc[item] = dc.get(item, 0) + 1
    
    return dc

def list_fighters(battle_data):
    fighters = set()
    
    for fighter, results in battle_data.items():
        fighters.add(fighter)
        fighters.update(results["loss"])
        fighters.update(results["win"])

    fighter_list = list(fighters)
    fighter_list.sort()

    return fighter_list

battle_data = {
    "Trisharp": {
        "loss": ["Togehug", "Psygoose"],
        "win": ["Pikabu", "Bulbizard"],
    },
    "Infernchimp": {
        "loss": ["Togehug", "Pikabu"],
        "win": ["Bulbizard", "Tehog"],
    },
    "Tehog": {
        "loss": ["Togehug", "Charasaur"],
        "win": ["Bulbizard", "Pikabu"]
    },
    "Psygoose": {
        "loss": ["Togehug", "Pikabu"],
        "win": ["Bulbizard", "Infernchimp"]
    },
}


