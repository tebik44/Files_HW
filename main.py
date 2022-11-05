import os
from pprint import pprint
# это для примера заданий --->

# cook_book_example = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

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


# 3 задание --->
def expansion():

    lst_files = []
    lst_file_path = []
    lst_names = []
    for i in os.listdir('tree_files'):
        lst_names.append(i)


    for item in lst_names:
        file_path_1 = os.path.join(os.getcwd() + r'\tree_files' + f'\{item}')
        lst_file_path.append(file_path_1)
        with open(file_path_1, encoding='UTF-8') as f:
            file_by = f.read().replace('\n', ' ')
            lst_files.append(file_by)

    insert_sort(lst_files, lst_file_path,lst_names)

def insert_sort (lst_files,lst_file_path, lst_names):
    for i in range(1, len(lst_files)):
        temp = lst_files[i]
        temp_2 = lst_names[i]
        temp_3 = lst_file_path[i]
        j = i - 1
        while (j >= 0 and temp > lst_files[j]):
            lst_files[j + 1] = lst_files[j]
            lst_names[j + 1] = lst_names[j]
            j = j - 1
        lst_files[j + 1] = temp
        lst_names[j + 1] = temp_2
    name_and_LENstring(lst_files, lst_names, lst_file_path)


def name_and_LENstring (lst_files, lst_names, lst_file_path):
    for i in range(0, len(lst_files)):
        pprint(f"Name file - {lst_names[i]}\nКолличество строк файла - {sum(1 for file in open(lst_file_path[i]))}\nИ конечно же сам файл - {lst_files[i]}")


#########################################################
# 3 задание я сделал автономным, вроде работает :)
#########################################################
print(expansion())








