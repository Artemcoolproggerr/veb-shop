food = ["бургер",'паста карбонара','суп овощной']
salads = ['цезарь','оливье','овощной','салат под шубой']
drinks = ['кока кола','фанта','газ.вода']
print('основные блюда:')
count = 1
for i in food:
    print('{}.{}'.format(count,i))
    count += 1
foods = input('выбирите основное блюдо: ')
print('-----------------')
print('салаты:')
count = 1
for d in salads:
    print('{}.{}'.format(count,d))
    count += 1
salad = input('выбирите салат: ')
print('-----------------')
print('напитки:')
count = 1
for a in drinks:
    print('{}.{}'.format(count,a))
    count += 1
drink = input('выбирите ваш напиток: ')
print('-----------------')
print('ваш заказ:')
print('основное блюдо: {}'.format(food[int(foods) - 1]))
print('салат: {}'.format(salads[int(salad) - 1]))
print('напиток: {}'.format(drinks[int(drink) - 1]))

