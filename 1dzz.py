duration = int(input('Введите время в секундах: '))
day = duration // (60 * 60 * 24)
hour = (duration - day * (60 * 60 * 24)) // (60 * 60)
minute = (duration - day * (60 * 60 * 24) - hour * (60 * 60)) // 60
second = duration - day * (60 * 60 * 24) - hour * (60 * 60) - minute * 60
print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')


list_number = []
for num in range(1, 1001, 2):
    list_number.append(num ** 3)

total_number = 0
for num in list_number:
    sum_number = 0
    for num_number in str(num):
        sum_number += int(num_number)
    if sum_number % 7 == 0:
        total_number += num
print(total_number)



