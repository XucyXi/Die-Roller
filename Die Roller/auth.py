
current_mode = 0

def check_mode():
    global current_mode
    return current_mode

def set_mode(new_mode):
    global current_mode
    current_mode = new_mode
    return current_mode