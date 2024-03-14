f = open('task3.txt', 'r')

N_M_Q = f.readline().split()
col_names = f.readline().split()

N, M, Q = list(map(int, N_M_Q))

matrix = dict()  # keys - col_names, values - columns

for row in range(N):
    matrix_row = f.readline().split()  # read matrix rows
    matrix_row = list(map(int, matrix_row))  # convert to int

    for m in range(M):
        if col_names[m] not in matrix.keys():
            matrix[col_names[m]] = [matrix_row[m]]  # add new cols to matrix
        else:
            matrix[col_names[m]].append(matrix_row[m])

for q in range(Q):
    col_name, symbol, criteria = f.readline().split()  # read request limits

    for row in range(N):
        if not (eval(f"{matrix[col_name][row]} {symbol} {criteria}")):  # check if criteria is not OK
            for column in matrix.values():
                column[row] = 0  # convert all bad rows elements to 0

fin_sum = 0
for column in matrix.values():
    fin_sum += sum(column)

print(fin_sum)

f.close()
