from pprint import pprint
cook_book_example = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
# class INcode_txt:
#   def __init__(self, file):
#       self.cook_book = {}
#       self.file = open('file.txt', encoding='UTF-8')

# 1 задание --->
cook_book = {}
def incode():
  with open('text.txt', 'r', encoding='UTF-8') as file:
      for dish in file:
        cook_book[dish.strip()] = []
        for item in range(int(file.readline())):
          items = list(file.readline().strip().split(' | '))
          cook_book[dish.strip()].append({'ingredient_name': items[0],'quantity': items[1],'measure': items[2]})
        file.readline()


# 2 задание --->
def get_shop_list_by_dishes(dishes, person_count):
    incode()
    cook_book_persone = {}
    lst = list()
    for dish in dishes:
        lst += cook_book.get(dish)

    new_dict = {}
    for old_dict in lst:
        key = old_dict.pop('ingredient_name')
        if key not in new_dict.keys():
            new_dict[key] = old_dict
        else:
            new_dict[key]: old_dict['quantity']

    for key, value in new_dict.items():
        print(f"{key}: {int(value['quantity']) * person_count} {value['measure']}")





get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)

# incode()
# pprint(cook_book)

