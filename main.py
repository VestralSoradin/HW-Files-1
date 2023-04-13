
def get_recipes(recipes_file='./recipes.txt'):
    cook_book = {}
    with open(recipes_file) as receipt_file:
        while True:
            dish = receipt_file.readline().rstrip('\n').lower()
            if not dish:
                break
            cook_book[dish] = []
            n = int(receipt_file.readline().rstrip('\n'))
            items = [receipt_file.readline().rstrip('\n').rsplit('|') for _ in range(n)]
            for item in items:
                cook_book[dish].append({'ingridient_name': item[0].rstrip(),
                                        'quantity': int(item[1].replace(' ', '')),
                                        'measure': item[2].replace(' ', '')})
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете '
                   'на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

cook_book = get_recipes()
create_shop_list(cook_book)

#def get_shop_list_by_dishes(dishes, person_count):
  #shop_list = {}
  #for dish in dishes:
    #for ingridient in cook_book[dish]:
      #new_shop_list_item = dict(ingridient)

      #new_shop_list_item['quantity'] *= person_count
      #if new_shop_list_item['ingridient_name'] not in shop_list:
        #shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      #else:
        #shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']


  #return shop_list


#def print_shop_list(shop_list):
  #for shop_list_item in shop_list.values():
    #print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            #shop_list_item['measure']))


#def create_shop_list():
  #person_count = int(input('Введите количество человек: '))
  #dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    #.lower().split(', ')
  #shop_list = get_shop_list_by_dishes(dishes, person_count)
  #print_shop_list(shop_list)


#create_shop_list()


#def my_cook_book():
  #with open('recipes.txt', encoding='utf-8') as file:
    #cook_book = {}
    #for txt in file.read().split('\n\n'):
      #name, _, *args = txt.split('\n')
      #tmp = []
      #for arg in args:
        #ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
        #tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
      #cook_book[name] = tmp
  #return cook_book


#dishes_dict = {}
#def get_shop_list_by_dishes(dishes, person_count):
    #for d in dishes:
        #for dd in cook_book.keys():
            #if d == dd:
                #for q in cook_book[dd]:
                    #q['cuantity'] *= person_count
                    #dishes_dict[q['ingredient_name']] = q
  #pprint(dishes_dict, sort_dict=False)
  #return dishes_dict

#new_dict = my_cook_book(['Запеченный картофель', 'Омлет', 2])
#print(new_dict)