PLAYER_OPTIONS = {
    'SEE_HAND': 1,
    'TAKE_CARD': 2,
    'FINISH': 3
}

def highlight_log(fn,):
    n = 40
    def wrapper(*args,**kwargs):
        print(f"\n{'#' * n}")
        res = fn(*args, **kwargs)
        print(f"{'#' * n}\n")
        return res
    
    return wrapper

def input_number_in_range(prompt: str, min: int, max: int) -> int:
    while True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print('Input a number')
            continue

        n = int(user_input)
        if n < min or n > max:
            print('Number out of range')
            continue

        return n

def input_in_list(prompt: str, options: list[str] | list[int]) -> str | int:
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