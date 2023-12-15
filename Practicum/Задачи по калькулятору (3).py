def concat(table1, table2):
    return table1 + table2

def split(table, row_number):
    table1 = table[:row_number]
    table2 = table[row_number:]
    return table1, table2

# Пример использования
table1 = [ [1, 2, 3], [4, 5, 6] ]
table2 = [ [7, 8, 9], [10, 11, 12] ]

concatenated_table = concat(table1, table2)
print(concatenated_table)

table3, table4 = split(concatenated_table, 1)
print(table3)
print(table4)

