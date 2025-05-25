def create_matrix(cell_values, x,y):
    state = [[[None] for i in range(x)] for j in range(y)]
    for i in range(x):
        for j in range(y):
            state[j][i] = cell_values[i * y + j]
    return state