from constants_container import dummy

def shift_row(state, direction):
    if direction == "left":
        for i in range(1,4):
            state[i] = state[i][i:] + state[i][:i]
    elif direction == "right":
        for i in range(1,4):
            state[i] = state[i][len(state[i])-i:] + state[i][:len(state[i])-i]
    return state

# print(shift_row(shift_row(dummy, 1), 0))