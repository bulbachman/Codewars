# sum_of_digits = 0
# input_string = ''
# digit = 1
# while digit != 0:
#     input_string = input("Введите целое число: ")
#     if input_string.isdigit():
#         digit = int(input_string)
#         sum_of_digits += digit
#     else:
#         print('Это не целое число!')
# print('Сумма чисел равна:', sum_of_digits)

a = 1
sum = 0
while a != 0:
    a = int(input("введите целое число:"))
    sum += a
print('сумма введенных чиcел',sum)
