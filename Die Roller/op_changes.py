heads_or_tails = None
chance_multiplier = 1.0

def get_hOrT():
    return heads_or_tails

def get_chance_multiplier():
    return chance_multiplier

def change_hOrT(new_choice):
    global heads_or_tails
    heads_or_tails = new_choice

def change_chance_multiplier(new_multiplier):
    global chance_multiplier
    chance_multiplier = new_multiplier

def reset_chances():
    global heads_or_tails, chance_multiplier
    heads_or_tails = None
    chance_multiplier = 1.0