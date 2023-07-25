def roll_call_dwarves(names):
    for planeteers in names:
        print(f"{names.index(planeteers) + 1}. {planeteers}")
    pass

def summon_captain_planet(elements):
    return [names.capitalize() + '!' for names in elements]
    pass
# call is what is in the array, each on of them
def long_planeteer_calls(calls):
    print(calls)
    for call in calls:
        if len(calls) > 4:
            return False
        else: 
            return True
    pass

def find_the_cheese(type):
    for taste in type:
        if taste == "cheddar" or taste == "gouda" or taste == "camembert":
            return taste
    pass
