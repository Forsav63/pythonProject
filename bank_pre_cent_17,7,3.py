per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму депозита:   '))
deposit = []
for k in per_cent: deposit.append(float(per_cent[k] * money / 100))
print(deposit)
print('Максимальная сумма, которорую вы можете заработать  ' + str(max(deposit)))

