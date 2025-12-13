
def menu(choices, title, quest):
   print(title)
   count = 1
   for i in choices:
       print('{}.{}'.format(count,i))
       count += 1
   choice = input(quest)
   print('-------------')
   return choices[int(choice) - 1]


food = ["бургер",'паста карбонара','суп овощной']
salads = ['цезарь','оливье','овощной','салат под шубой']
drinks = ['кока кола','фанта','газ.вода']
main_food =  menu(food, 'основные блюда:', 'выберите основное блюдо: ')
my_salad = menu(salads, 'салаты:', 'выберите салат: ')
my_drink = menu(drinks, 'напитки:', 'выберите напиток: ')
print('ваш заказ:')
print('основное блюдо: {}'.format(main_food))
print('салаты: {}'.format(my_salad))
print('напиток: {}'.format(my_drink))















