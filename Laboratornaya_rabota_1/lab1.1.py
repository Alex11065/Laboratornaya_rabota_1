numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_numbers = 4  # производим замену none
sum_numbers = sum(numbers[:index_numbers]) + sum(numbers[index_numbers + 1:]) # считаем их сумму
count_numbers = len(numbers) # подсчет колличества
avg_ = sum_numbers / count_numbers # средне арифметическое
numbers[index_numbers] = avg_ # подставлям среднеарифмитическое
print("Измененный список:", numbers)
