from banners import banner_choices, get_banner_index
import os
from colors import colors

RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET = colors()

def get_banner():
    banners = banner_choices()
    return print(banners[get_banner_index()],f"\n{'Made by Xucy':>60}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def default_menu():
    get_banner()
    print("Type 1 to flip a coin")
    print("Type 2 to die roll")
    print("Type 3 to change mode")
    print("Type 4 to end program\n")
    return input(f"\nYour choice: ").lower()

def operator_menu():
    get_banner()
    print("Type 1 to flip a coin")
    print("Type 2 to die roll")
    print("Type 3 to change mode")
    print("Type 4 to change the die or coin chances")
    print("Type 5 to end program")
    return input(f"\nYour choice: ").lower()

def change_mode_menu():
    get_banner()
    print("Type 1 for default mode")
    print("Type 2 for Donnyboo mode")
    return input("\nYour choice: ")

def change_mode_result(new_mode):
    get_banner()
    print(f"Mode changed to {'Donnyboo' if new_mode == 1 else 'Default'} mode.\n")
    
def change_mode_easter_egg(new_mode):
    get_banner()
    print(f"Mode changed to {'67' if new_mode == 67 else '69'} easter egg.\n")

def coin_flip_result(result):
    get_banner()
    print(f"You flipped a {result}!\n")

def die_roll_amount():
    get_banner()
    return int(input("Enter the maximum die amount (e.g., 6 for a d6): "))

def die_roll_result(result, max_amount):
    get_banner()
    print(f"You rolled a {result} out of {max_amount}!\n")

def change_chances_menu():
    get_banner()
    print("Type 'heads' or 'tails' to set the coin flip choice bias")
    print("Type a float number (e.g., 1.5) to set the die roll chance multiplier")
    print("Type 'reset' to reset chances to default\n")
    return input("Your choice: ").lower()

def enter_to_continue():
    input(f"\nPress Enter to continue...")

def error_message():
    print(f"{RED}Invalid input. Please try again.{RESET}\n")

def end_message():
    print(f"{GREEN}Ending program! Goodbye!{RESET}\n")