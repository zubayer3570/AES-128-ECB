def add_round_key(state, key):
    for i in range(len(state)):
        for j in range(len(state[0])):
            state[i][j] = hex(int(state[i][j], 16) ^ int(key[i][j], 16))[2:].zfill(2)
    return state

