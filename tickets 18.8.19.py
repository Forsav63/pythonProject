cost = 0
number_of_tickets = int(input('Введите цифрами количество билетов: \n'))
for i in range(number_of_tickets):
    i += 1
    age = int(input(f'Введите цифрами количество полных лет {i} посетителя: \n'))
    if age < 18:
            print('Цена билета  0 руб.')
    elif 18 <= age < 25:
            cost += 990
            print('Цена билета  990 руб.')
    else:
            cost += 1390
            print('Цена билета  1390 руб.')
if number_of_tickets > 3:
    total_cost = 0.9*cost
    print(f'Сумма к оплате  {total_cost} руб.')
else:
    print(f'Сумма к оплате  {cost} руб.')







