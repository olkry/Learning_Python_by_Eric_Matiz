# for number in range(1,21):
#     print(number)

# million_number = [i for i in range(1, 1000001)]
# # for number in million_number:
# #     print(number)
#
# print(min(million_number))
# print(max(million_number))
# print(sum(million_number))

# odd_numbers = [i for i in range(1, 21, 2)]
# for numb in odd_numbers:
#     print(numb)

# multiples_of_three = [i for i in range(3, 31, 3)]
# for numb in multiples_of_three:
#     print(numb)

cube = [i ** 3 for i in range(1, 11)]
print(cube)
# for num in cube:
#     print(num)
print(f'Первые 3 числа:      {cube[:3]}')
print(f'3 числа из середины: {cube[3:6]}')
print(f'Последние 3 числа:   {cube[-3:]}')