def roll_call_dwarves(dwarfs):
    dwarf_list = [f"{index}. {dwarf}" for index, dwarf in enumerate(dwarfs, 1)]

    for dwarf in dwarf_list :
        print(dwarf)




def summon_captain_planet(planeeters):
    planeteer_list = []

    for planetter in planeeters :
        planeteer_list.append(planetter.capitalize() + "!")

    return planeteer_list




def long_planeteer_calls(calls):
    character_length = any(len(call) > 4 for call in calls)

    return character_length




def find_the_cheese(food):
    cheese = ["american", "cheddar", "swiss"]

    found = "no"

    for item in food :
        if item in cheese :
            found = "yes"
            return item
        if not found :
            return None

