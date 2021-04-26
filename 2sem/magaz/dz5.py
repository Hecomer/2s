from datetime import datetime


class Shop:
    def __init__(self, products, prices, quantity, name):
        self.products = products
        self.prices = prices
        self.quantity = quantity
        self.name = name
        self.shop, self.product, self.count, self.save_check = None, None, None, None

    def user_buy(self, product_name, count, user_name, save_check=False):
        index = 0
        while product_name != self.products[index]:
            index += 1

        if count > 0:
            if self.quantity[index] >= count:
                self.quantity[index] -= count
            else:
                print("В магазине меньшее кол-во товара, что Вы просите")
            if save_check is True:
                date_and_time = str(datetime.today()).split()
                date = date_and_time[0]
                time = date_and_time[1][:8]
                time = [x for x in time]
                for _ in time:
                    if _ == ':':
                        time[time.index(_)] = '-'
                time = ''.join(time)

                with open(f"{user_name}_{date}_{time}.txt", "w", encoding='utf-8') as file:
                    file.write(f'купленный товар: {product_name}\nкол-во товара: {count}\nмагазин: {self.name}')
                file.close()
            print('Покупка успешно совершена')
        else:
            print("Не вижу смысла в Вашей покупке")
        self.counting()

    def counting(self):
        for i in range(len(self.quantity)):
            if self.quantity[i] == 0:
                del self.products[i]
                del self.prices[i]

def sort_shops_by_product_price(product):
    price_lst = []
    shops_with_product = find_product(product, False) # ищет магазины, в которых есть этот продукт
    for i in shops_with_product:
        for j in shops:
            if j.name == i:
                price_lst.append(j.prices[j.products.index(product)])
        # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
        # индексом цена этого продукта из списка цен
    for j in range(len(shops_with_product)):
        print(f'{shops_with_product[price_lst.index(min(price_lst))]}: {min(price_lst)} рублей')
        if len(price_lst) > 1:
            index_for_delete = price_lst.index(min(price_lst))
            price_lst.pop(index_for_delete)
            shops_with_product.pop(index_for_delete)

def sort_shops_by_product_count(product):
    quantity_lst = []
    shops_with_product = find_product(product, False)  # ищет магазины, в которых есть этот продукт
    for i in shops_with_product:
        for j in shops:
            if j.name == i:
                quantity_lst.append(j.quantity[j.products.index(product)])
        # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
        # индексом цена этого продукта из списка цен
    for j in range(len(shops_with_product)):
        print(f'{shops_with_product[quantity_lst.index(max(quantity_lst))]}: {max(quantity_lst)} штук')
        if len(quantity_lst) > 1:
            index_for_delete = quantity_lst.index(max(quantity_lst))
            quantity_lst.pop(index_for_delete)
            shops_with_product.pop(index_for_delete)


def find_product(product_name, should_i_print=True, count=0):
    useful_shops = []
    for i in shops:
        for j in range(len(i.products)):
            if (i.products[j] == product_name) and (i.quantity[j] > count):
                useful_shops.append(i.name)
    if should_i_print is True:
        if len(useful_shops) != 0:
            print(*useful_shops, sep='\n')
        else:
            print('Такого не продаем -_-')
    return useful_shops

def find_products(products):
    very_useful_shops = []
    for i in shops:
        very_useful_shops.append(i.name)
    for i in products:
        useful_shops = []
        for j in shops:
            for z in range(len(j.products)):
                if j.products[z] == i:
                    useful_shops.append(j.name)
        for j in very_useful_shops:
            if j not in useful_shops:
                very_useful_shops.remove(j)
    if len(very_useful_shops) != 0:
        print(*very_useful_shops, sep='\n')
    else:
        print('Таких товаров нет в одном магазине')


def buy(shop, product, count, user_name, save_check=False):
    shop.user_buy(product, count, user_name, save_check=save_check)


def save_changes(file_name):
    file = open(file_name + '.txt', 'w', encoding='utf-8')
    for shop in shops:
        products = ','.join(shop.products)
        file.write(';'.join([shop.name, products, str(shop.prices), str(shop.quantity)]) + '\n')


def load_data(file_name, rewrite=True):
    with open(file_name + '.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.split(';')
            name = line[0]
            products = line[1].split(',')
            prices = list(map(int, line[2][1:-1].split(', ')))
            quantity = list(map(int, line[3][1:-2].split(', ')))

            for shop in shops:
                if shop.name == name:
                    if rewrite:
                        shop.products = products
                        shop.prices = prices
                        shop.quantity = quantity

shops = [
    Shop(['бояринъ', 'телевизор', 'велосипед', 'зубная паста', 'вода', 'шампунь', 'гель для душа'],
         [300, 100, 5000, 58, 7, 120, 300],
         [18, 50, 102, 33, 78, 4, 80],
         'Ozon671Shop'),
    Shop(["бритва", "робот-пылесос", "масло", "свечи", "мороженное", "паста", "косметичка", "вода"],
         [5000, 3100, 1999, 300, 100, 9999, 2700, 900],
         [4, 9, 2, 10, 2, 4, 8, 42],
         'Brojob'),
    Shop(["таблетки для посудомоечной машины", "дверная ручка", "маска", "ручка", "принтер", "вода", "сумка", "тетрадь"],
         [10000, 23000, 9999, 10, 3467, 9123, 4823, 79999],
         [10, 2, 1, 3700, 12, 8, 1000],
         'Aboba'),
    Shop(["градусник", "хлеб", "тетрадь", "карандаш", "вода", "каподастр", "комплект постельного белья", "маска",
          "футболка с принтом крутой лягушки", "кепка"],
         [34, 20, 400, 50, 20, 100, 49, 99, 1999, 1],
         [8, 12, 50, 17, 100, 288, 43, 35, 9, 102323],
         'Свинолошадь')
]
load_data('data')

print("Здравствуйте, зачем пожаловали?")
while True:
    print("Введите цифру, соответствующую вашему запросу:\n", "1. Купить товар\n",
      "2. Поиск по товару\n", "3. Поиск по товарам\n", "4. Сортировка по цене товара\n",
          "5. Сортировка по количеству товара")
    que = int(input("Ответ: "))
    if que == 1488:
        print('Теперь вам доступна власть богов')
    if que == 1:
        print("Введите через пробел номер магазина(где 1 - Moydodyr, 2 - Bigboyshop, 3 - Prada, 4 - Nezachetochka)"
              ", название товара, количество товара и свое имя."
              " Также ответьте на вопрос: нужен ли вам чек (да/нет)")
        ans = input()
        ans_spl = list(ans.lower().split())
        if len(ans_spl) == 5:
            if ans_spl[4] == "да":
                buy(shops[int(ans_spl[0]) - 1], ans_spl[1], int(ans_spl[2]), ans_spl[3], True)
                save_changes("data")
            else:
                buy(shops[int(ans_spl[0]) - 1], ans_spl[1], int(ans_spl[2]), ans_spl[3], False)
                save_changes("data")
        else:
            print("Вызовите охрану...")
            break
    elif que == 2:
        prod = input("Введите название товара: ")
        find_product(prod)
    elif que == 3:
        ans1 = input("Введите названия товаров через пробел: ")
        ans_spl1 = list(ans1.lower().split())
        find_products(ans_spl1)
    elif que == 4:
        prod = input("Введите название товара: ")
        sort_shops_by_product_price(prod)
    elif que == 5:
        prod = input("Введите название товара: ")
        sort_shops_by_product_count(prod)
    else:
        print('Я не до конца понял ваш запрос')
    final = input("Хотите вернуться к выбору опции?(да/нет)\n").lower()
    if final == "нет":
        break
    elif final == 'да':
        continue
    else:
        print('ты чево наделал...')
        break