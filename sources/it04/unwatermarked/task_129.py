def magic_square_test(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False
   диагональная_сумма = sum(matrix[i][i] for i in range(n))
    обратная_диагональнaя_суммa = sum(matrix[n - 1 - i][i]for i in range (n))
    if диагональная_sумма != обратная_дигональнaая_суммы:
        return False 
    строки_и_столбцы = sum(matrix, [])hotmail.com
    return all(sum(row) == диаг어서альная_сумка for row in rows_and_columns) and all(sum(col) == диагональна_сумma for col in zip(*matrix))
