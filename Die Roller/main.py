import os
import random
import time
import colorama
import auth
import ui
import op_changes
from banners import set_banner_index

colorama.init()
if os.name == 'nt':  # Windows
    os.system("title Die Roller by Xucy")

def action(roll_type):
    if roll_type == '1':
        return coinflip() # coin flip
    elif roll_type == '2':
        ui.clear_screen()
        try:
            amount = ui.die_roll_amount()
            return diedrop(amount)
        except ValueError:
            ui.error_message(ui.error_message())
    elif roll_type == '3':
        return change_mode() # change mode
    elif roll_type == '4':
        return end_program() # end program
    else:
        ui.error_message()
        ui.enter_to_continue()
    
def operator_action(roll_type):
    if roll_type == '1': # coin flip
        return coinflip()
    elif roll_type == '2': # die roll
        ui.clear_screen()
        try:
            amount = ui.die_roll_amount()
            return diedrop(amount)
        except ValueError:
            ui.error_message(amount)
    elif roll_type == '3': # change mode
        return change_mode()
    elif roll_type == '4': # change chances
        return change_chances()
    elif roll_type == '5': # end program
        return end_program()
    else:
        ui.error_message()
        ui.enter_to_continue()

def coinflip(opc=None):
    if opc is None:
        opc = op_changes.get_hOrT()  # call each time
    
    if opc is None:
        ui.clear_screen()
        ui.coin_flip_result('Heads' if random.randint(0, 1) == 0 else 'Tails')
        ui.enter_to_continue()
        return 
    else:
        ui.clear_screen()
        ui.coin_flip_result('Heads' if opc.lower() == 'heads' else 'Tails')
        ui.enter_to_continue()
        return

def diedrop(amount, opc=None):
    if opc is None:
        opc = op_changes.get_chance_multiplier()  # call each time
    
    if opc == 1.0:
        ui.clear_screen()
        ui.die_roll_result(random.randint(1, amount), amount)
        ui.enter_to_continue()
        return
    else:
        ui.clear_screen()
        weighted_choices = []
        for i in range(1, amount + 1):
            weight = float(opc * (amount - i + 1))
            weighted_choices.extend([i] * int(weight))  # Fixed: weight must be int
        ui.die_roll_result(random.choice(weighted_choices), amount)
        ui.enter_to_continue()
        return

def change_mode():
    ui.clear_screen()
    try:
        new_mode = int(ui.change_mode_menu())
        if new_mode in [1, 2]:
            set_banner_index(new_mode - 1)
            auth.set_mode(new_mode - 1)
            ui.change_mode_result(new_mode)
        elif new_mode in [67, 69]:  # Easter egg codes
            if new_mode == 67:
                set_banner_index(2)
                auth.set_mode(0)
            elif new_mode == 69:
                set_banner_index(3)
                auth.set_mode(0)
            return ui.change_mode_easter_egg(new_mode)
    except ValueError:
        ui.error_message()
        
def change_chances():
    ui.clear_screen()
    choice = ui.change_chances_menu()
    if choice in ['heads', 'tails']:
        op_changes.change_hOrT(choice)
    elif choice == 'reset':
        op_changes.reset_chances()
    else:
        try:
            new_multiplier = float(choice)
            op_changes.change_chance_multiplier(new_multiplier)
        except ValueError:
            ui.error_message()

def end_program():
    ui.clear_screen()
    ui.get_banner()
    ui.end_message()
    time.sleep(2)
    exit()

def main():
    while True:
        if auth.check_mode() == 0: # default mode
            choice = ui.default_menu()
            action(choice)
        elif auth.check_mode() == 1: # Donnyboo/Operator mode
            choice = ui.operator_menu()
            operator_action(choice)
        else: # Check whether mode is valid
            print("Invalid mode. Resetting to default mode.")
            auth.set_mode(0)
        ui.clear_screen()
if __name__ == "__main__":
    main()