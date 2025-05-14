import numpy
from constants_container import sbox, RC

def expansion_key(key):
    words = [key[i:i + 8] for i in range(0, len(key), 8)]
    count = 0
    for i in range(4, 44):
        if i % 4 == 0:
            # 1 byte left shift
            word_bytes = [words[i - 1][j:j + 2] for j in range(0, len(words[i - 1]), 2)]
            word_bytes.append(word_bytes[0])
            word_bytes = word_bytes[1:]

            # # substitiute byte
            for k in range(len(word_bytes)):
                # word_bytes[k] = sub_byte(word_bytes[k])
                x = int(word_bytes[k][0], 16)
                y = int(word_bytes[k][1], 16)
                word_bytes[k] = hex(sbox[x][y])[2:].zfill(2)

            # XOR with RC[i]
            word_bytes[0] = hex(int(word_bytes[0], 16) ^ RC[count])[2:].zfill(2)

            output = hex(int("".join(word_bytes), 16) ^ int(words[i - 4], 16))[2:].zfill(8)
            words.append(output)
            count += 1
        else:
            output = hex(int(words[i - 1], 16) ^ int(words[i - 4], 16))[2:].zfill(8)
            words.append(output)

    words_list = [words[i:i+4] for i in range(0, len(words), 4)]
    for i in range(len(words_list)):
        for j in range(len(words_list[0])):
            words_list[i][j] = [words_list[i][j][k:k+2] for k in range(0, len(words_list[i][j]), 2)]

    for i in range(len(words_list)):
        temp = words_list[i]
        n_arr = numpy.array(temp)
        words_list[i] = n_arr.T

    return words_list