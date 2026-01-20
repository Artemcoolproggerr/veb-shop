def menu_from_files(name_file):
    choices = open(name_file,'r',encoding='utf-8')
    result = []
    reading = choices.readlines()
    for i in reading:
        result.append(i.rstrip('\n'))
    return result





def menu(choices, title, question):
   print(title)
   count = 1
   for i in choices:
       print('{}.{}'.format(count,i))
       count += 1
   print('для того чтобы сделать заказ введите номер блюда')
   choice = input(question)
   print('-' * len(question))
   while True:
       allowed_answers = []
       for i in range(1, len(choices) + 1):
           allowed_answers.append(str(i))
       allowed_answers.append('x')
       if choice in allowed_answers:
           if choice == 'x':
               answer = '----------'
               break
           answer = choices[int(choice) - 1]
           break
       else:
           print('НЕккорктный ввод!введите число от 1 до {}'.format(len(choices)))
           choice = input(question)
   return answer




food = menu_from_files('main food.txt')
salads = menu_from_files('salads.txt')
drinks = menu_from_files('drinks.txt')
main_food =  menu(food, 'основные блюда:', 'выберите основное блюдо: ')
my_salad = menu(salads, 'салаты:', 'выберите салат: ')
my_drink = menu(drinks, 'напитки:', 'выберите напиток: ')
print('ваш заказ:')
print('основное блюдо: {}'.format(main_food))
print('салаты: {}'.format(my_salad))
print('напиток: {}'.format(my_drink))





















