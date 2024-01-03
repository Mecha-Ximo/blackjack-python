def highlight_log(fn):
    def wrapper(*args,**kwargs):
        print(f"\n{'#' * 20}")
        res = fn(*args, **kwargs)
        print(f"{'#' * 20}\n")
        return res
    
    return wrapper