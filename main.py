from add_round_key import add_round_key
from key_expansion import expansion_key
from mix_col import mix_column
from shift_rows import shift_row
from state_creator import create_states
from sub_byte_state import sub_byte_state
from constants_container import mix_columns_matrix, sbox, inv_sbox, inv_mix_columns_matrix
from Crypto.Util.Padding import unpad

def encryption(plainText, key):
    all_keys = expansion_key(key=key)

    states = create_states(plainText, "enc")

    for i in range(len(states)):
        state = states[i]
        # initial round
        state = add_round_key(state, all_keys[0])

        for j in range(9):
            state = sub_byte_state(state, sbox)
            state = shift_row(state, "left")
            state = mix_column(state, mix_columns_matrix)
            state = add_round_key(state, all_keys[j + 1])

        # last round
        state = sub_byte_state(state, sbox)
        state = shift_row(state, "left")
        state = add_round_key(state, all_keys[10])
        states[i] = state
    cipherText = ""
    for i in range(len(states)):
        for j in range(len(states[0])):
            for k in range(len(states[0][0])):
                cipherText += states[i][k][j]
    return cipherText

def decryption(cipherText, key):
    all_keys_rev = expansion_key(key=key)
    all_keys = all_keys_rev[::-1]

    states = create_states(cipherText, "dec")

    for i in range(len(states)):
        state = states[i]
        # initial round
        state = add_round_key(state, all_keys[0])

        for j in range(9):
            state = shift_row(state, "right")
            state = sub_byte_state(state, inv_sbox)
            state = add_round_key(state, all_keys[j + 1])
            state = mix_column(state, inv_mix_columns_matrix)

        # last round
        state = shift_row(state, "right")
        state = sub_byte_state(state, inv_sbox)
        state = add_round_key(state, all_keys[10])
        states[i] = state
    # print(states)
    plainText = ""
    for i in range(len(states)):
        for j in range(len(states[0])):
            for k in range(len(states[0][0])):
                plainText += states[i][k][j]
    blockSize = 16
    return unpad(bytes.fromhex(plainText), blockSize).hex()

# Interactive mode
task = input("------------AES 128 (ECB)------------? \n1.Encryption\n2.Decryption\nChoose: ")
if task == "1":
    plaintext = input("Enter Plaintext (utf-8): ")
    key = input("Enter Key (utf-8): ")
    if (len(key) != 16):
        print("Invalid Key Length!!!")
    else:
        plaintext = plaintext.encode().hex()
        key = key.encode().hex()
        print("CipherText (hex value):", encryption(plaintext, key))
elif task == "2":
    ciphertext = input("Enter Ciphertext (hex value): ")
    key = input("Enter Key (utf-8): ")
    if (len(key) != 16):
        print("Invalid Key Length!!!")
    else:
        hex_plainText = decryption(ciphertext, key.encode().hex())
        plainText = bytes.fromhex(decryption(ciphertext, key.encode().hex())).decode()
        print("PlainText (utf-8):", plainText)
else:
    print("Invalid Input!!!\n")


# # # Testing
# plainText = "0123456789abcdeffedcba9876543210"
# key = "0f1571c947d9e8590cb7add6af7f6798"
# enc_cipherText = encryption(plainText, key)
# dec_plainText = decryption(enc_cipherText, key)
#
# print("PlainText(hex): ", plainText)
# print("Encrypted(hex): ", enc_cipherText)
# print("Decrypted(hex): ", dec_plainText)
#
# if plainText == dec_plainText:
#     print("Worked!")

