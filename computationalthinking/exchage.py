have_money = 2500000
exchange_rate = 1175
#exchange_money = 2127
#left_money = 775

exchange_money = have_money / exchange_rate
print(exchange_money)
left_money = have_money % exchange_rate
print(left_money)

print("가진돈:", have_money)
print("환율:", exchange_rate)
print("환전액:", exchange_money)
print("남은돈:", left_money)