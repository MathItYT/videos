arr = [1, 2, -5, 6, 9, 8, 5, -1, -2, 17]
# Inicializando la variable max_sum
max_sum = 0

for i in range(len(arr) - 4):
    arr_sum = sum(arr[i:i + 5])
    if arr_sum > max_sum:
        max_sum = arr_sum