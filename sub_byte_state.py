from constants_container import sbox, inv_sbox, dummy

def sub_byte_state(state, sub_box):
    for i in range(len(state)):
        for j in range(len(state[0])):
            x = int(state[i][j][0], 16)
            y = int(state[i][j][1], 16)
            state[i][j] = hex(sub_box[x][y])[2:].zfill(2)
    return state

# print(sub_byte_state(sub_byte_state(dummy, sbox), inv_sbox))
