import time

a = 7658347
c = 12345
m = 2**31
seed = time.time_ns()+1
state = seed % m

def _next_raw() -> int:
    global state
    state = (a * state + c) % m
    return state

def randint(min_val: int, max_val: int) -> int:
    raw = _next_raw()
    return min_val + raw % (max_val - min_val + 1)

def random():
    return _next_raw()

def randfloat(min_val=0.0, max_val=1.0) -> float:
    raw = _next_raw()  # integer in [0, m)
    unit = raw / m  # float in [0, 1)
    return min_val + unit * (max_val - min_val)
