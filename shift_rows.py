import numpy as np
from constants_container import dummy

def shift_row(state: np.ndarray, direction):
    if direction == 1:
        for i in range(1,4):
            state[i] = np.roll(state[i], -i)
    elif direction == 0:
        for i in range(1,4):
            state[i] = np.roll(state[i], i)
    return state

# print(shift_row(shift_row(dummy, 1), 0))