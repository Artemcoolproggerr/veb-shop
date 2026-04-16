import foods

def main():
    order = foods.get_order()
    # two = order.get('main food')
    # three = order.get('salad')
    # four = order.get('drink')
    # print('{} ваш заказ: '.format(one))
    # print('основное блюдо: {}'.format(two))
    # print('салаты: {}'.format(three))
    # print('напиток: {}'.format(four))
    for key, value in order.items():
        print(f"{key}: {value}")
    print('Итого:-------------')



if __name__== "__main__":
    main()

