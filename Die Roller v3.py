import os
import random

def coinflip():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

def diedrop(amount):
    return random.randint(1, amount)

def main():
    # ANSI color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    banner = rf"""{BLUE}
________  .__         __________       .__  .__                
\______ \ |__| ____   \______   \ ____ |  | |  |   ___________ 
 |    |  \|  |/ __ \   |       _//  _ \|  | |  | _/ __ \_  __ \
 |    `   \  \  ___/   |    |   (  <_> )  |_|  |_\  ___/|  | \/
/_______  /__|\___  >  |____|_  /\____/|____/____/\___  >__|   
        \/        \/          \/                      \/       {RESET}"""
    
    banner1 = rf"""{CYAN}
  _________________     __________         .__   .__                   
 /  _____/\______  \    \______   \  ____  |  |  |  |    ____ _______  
/   __  \     /    /     |       _/ /  _ \ |  |  |  |  _/ __ \\_  __ \ 
\  |__\  \   /    /      |    |   \(  <_> )|  |__|  |__\  ___/ |  | \/ 
 \_____  /  /____/       |____|_  / \____/ |____/|____/ \___  >|__|    
       \/                       \/                          \/         {RESET}"""
    banner2 = rf"""{MAGENTA}
 _______  .__                 __________       .__  .__                  ________________ 
 \      \ |__| ____  ____     \______   \ ____ |  | |  |   ___________  /  _____/   __   \
 /   |   \|  |/ ___\/ __ \     |       _//  _ \|  | |  | _/ __ \_  __ \/   __  \\____    /
/    |    \  \  \__\  ___/     |    |   (  <_> )  |_|  |_\  ___/|  | \/\  |__\  \  /    / 
\____|__  /__|\___  >___  >____|____|_  /\____/|____/____/\___  >__|____\_____  / /____/  
        \/        \/    \/_____/      \/                      \/  /_____/     \/          {RESET}"""
    
    banner3 = rf"""{RED}
________                              ___.                        _____             .___      
\______ \   ____   ____   ____ ___.__.\_ |__   ____   ____       /     \   ____   __| _/____  
 |    |  \ /  _ \ /    \ /    <   |  | | __ \ /  _ \ /  _ \     /  \ /  \ /  _ \ / __ |/ __ \ 
 |    `   (  <_> )   |  \   |  \___  | | \_\ (  <_> |  <_> )   /    Y    (  <_> ) /_/ \  ___/ 
/_______  /\____/|___|  /___|  / ____| |___  /\____/ \____/____\____|__  /\____/\____ |\___  >
        \/            \/     \/\/          \/            /_____/       \/            \/    \/ {RESET}"""
    
    banners = [banner, banner1, banner2, banner3]
    i = 0 # banner index

    while True:
        print(banners[i],f"\n{'Made by Xucy':>60}\n")
        ask = input(f"Type 1 for coinflip\nType 2 for die roll\nType 3 to end program\n\nYour choice: " if i == 0 else f"Type 1 for coinflip\nType 2 for die roll\nType 3 to end program\nType 'exit' to exit easter egg mode\n\nYour choice: ").lower()
        if ask == "1":
            result = coinflip()
            print(f"You flipped {result}.\n")
            c = input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif ask == "2":
            try:
                sides = int(input("Enter the number of sides on the die: "))
                result = diedrop(sides)
                print(f"You rolled a {result} on a {sides}-sided die.\n")
                c = input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                c = input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
        elif ask == "3":
            print("Ending program.")
            break
        elif ask == "exit":  # exit easter egg
            i = 0
            os.system('cls' if os.name == 'nt' else 'clear')
        elif ask == "67":  # easter egg
            i = 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Invalid choice. Please try again.\n")
            c = input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    main()