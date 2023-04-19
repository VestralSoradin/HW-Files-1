import os
from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding='utf-8') as src_file:
    last_key = ''
    for line in src_file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            last_key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))


dishes_dict = {}
def get_shop_list_by_dishes(dishes, person_count):
     for d in dishes:
         for dd in cook_book.keys():
             if d == dd:
                 for q in cook_book[dd]:
                     q['quantity'] *= person_count
                     dishes_dict[q['ingredient_name']] = q
                     #dishes_dict.append(q)
     pprint(dishes_dict,sort_dicts=False)
     return dishes_dict
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
