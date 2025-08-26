food = ["бургер",'пааста карбонара','суп овощной']
salads = ['цезарь','оливье','овощной','салат под шубой']
drinks = ['кока кола','фанта','газ.вода']
print('основные блюда:')
count = 1
for i in food:
    print('{}.{}'.format(count,i))
    count += 1
print('-----------------')
print('салаты:')
count = 1
for d in salads:
    print('{}.{}'.format(count,d))
    count += 1
print('-----------------')
print('напитки:')
count = 1
for a in drinks:
    print('{}.{}'.format(count,a))
    count += 1