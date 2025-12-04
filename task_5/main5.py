num = int(input("введите любое целое число: "))

if num >= 0:
    abs_num = num
else: 
    abs_num = -(-num)
print("абсолютное значение числа : ", abs_num)