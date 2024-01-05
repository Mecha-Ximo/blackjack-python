PLAYER_OPTIONS = {
    'SEE_HAND': 1,
    'SEE_HAND_VALUE': 2,
    'TAKE_CARD': 3,
    'FINISH': 4
}

def highlight_log(fn,):
    n = 40
    def wrapper(*args,**kwargs):
        print(f"\n{'#' * n}")
        res = fn(*args, **kwargs)
        print(f"{'#' * n}\n")
        return res
    
    return wrapper

def input_with_validation(prompt: str, options: list[str] | list[int]) -> str | int:
    while True:
        user_input = input(prompt)

        if type(options[0]) == str:
            if user_input in options:
                return user_input
        if type(options[0]) == int:
            if user_input.isdigit():
                int_input = int(user_input)
                if int_input in options:
                    return int_input
        
        print("Invalid input")