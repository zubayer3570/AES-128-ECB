from constants_container import mix_columns_matrix, inv_mix_columns_matrix, dummy

def handle_0x02(num:int):
    flag = bin(num)[2:].zfill(8)[0]
    num = (num << 1) & 0xFF
    if flag == "1":
        num = num ^ 0x1B
    return num

def mix_column(state, mix_columns_matrix):
    mixed_matrix = [[[0] for i in range(4)] for i in range(4)]
    for i in range(len(mix_columns_matrix)):
        for j in range(len(state[0])):
            result = 0
            for k in range(len(mix_columns_matrix[0])):
                m_1 = mix_columns_matrix[i][k]
                m_2 = int(state[k][j], 16)
                temp = 0
                # for forward mix
                if m_1 == 1:
                    temp = m_2
                elif m_1 == 2:
                    temp = handle_0x02(m_2)
                elif m_1 == 3:
                    temp = (m_2 ^ handle_0x02(m_2))

                # for inverse mix
                elif m_1 == 9:
                    temp = handle_0x02(handle_0x02(handle_0x02(m_2)))^m_2
                elif m_1 == 11:
                    temp = handle_0x02(handle_0x02(handle_0x02(m_2))^m_2)^m_2
                elif m_1 == 13:
                    temp = handle_0x02(handle_0x02(handle_0x02(m_2)^m_2))^m_2
                elif m_1 == 14:
                    temp = handle_0x02(handle_0x02(handle_0x02(m_2)^m_2)^m_2)

                result ^= temp
            mixed_matrix[i][j] = hex(result)[2:].zfill(2)
    return mixed_matrix

# print(mix_column(mix_column(dummy, mix_columns_matrix), inv_mix_columns_matrix))
