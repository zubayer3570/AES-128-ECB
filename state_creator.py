from Crypto.Util.Padding import pad
import numpy as np

def add_padding(plainText:str, blockSize):
    return pad(bytes.fromhex(plainText), blockSize).hex()

def create_state(block:str):
    cell_values = [block[i:i+2] for i in range(0, len(block), 2)]
    np_arr = np.array(cell_values)
    state = np_arr.reshape(4,4).T # transposing because in AES, the elements are organized by column
    return state

def create_blocks(plainText:str):
    return [plainText[i:i+32] for i in range(0, len(plainText), 32)]

def create_states_enc(text:str, flag):
    blocks = None
    if flag == "enc":
        blocks = create_blocks(add_padding(text, 16))
    elif flag == "dec":
        blocks = create_blocks(text)

    states = []
    for block in blocks:
        state = create_state(block)
        states.append(state)
    return states