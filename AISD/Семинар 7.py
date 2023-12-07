
#1) На основе переданной строки (не содержащей повторяющихся символов) создать словарь,
# в котром каждому символу строки будет соответствовать номер символа в строке. Пример: строка 'abcdef'

def create_dict(string):
    # Создаем пустой словарь
    result = {}

    # Используем функцию enumerate() для получения индекса и символа строки
    for index, char in enumerate(string):
        # Добавляем символ и его индекс в словарь
        result[char] = index
    return result


# Пример использования функции
input_string = 'abcdef'
result_dict = create_dict(input_string)
print(result_dict)


#2)
# Для определения количества элементов заданного списка, содержащихся в словаре, можно использовать пересечение множеств. 
def count_list_elements_in_dict(input_list, input_dict):
    # Используем операцию пересечения множеств, чтобы найти общие элементы
    common_elements = set(input_list) & set(input_dict.keys())

    return len(common_elements)


# Пример использования функции
l1 = [1, 2, 3, 4, 5, 6, 7]
d1 = {1: 'a', 2: 'b', 3: 'c', 6: 'd'}
result = count_list_elements_in_dict(l1, d1)
print(result)



#3) Чтобы создать словарь, в котором для каждого символа строки будет храниться число: сколько раз символ встретился в строке, можно использовать цикл для прохода по каждому символу строки. Для хранения числа встреч символа можно использовать словарь, где ключами будут символы строки, а значениями - количество их встреч.

def create_char_count_dict(input_string):
    # Создаем пустой словарь
    char_count_dict = {}
    
    # Проходим по каждому символу строки
    for char in input_string:
        # Проверяем, есть ли символ в словаре
        if char in char_count_dict:
            # Если символ уже встречался, увеличиваем его счетчик на 1
            char_count_dict[char] += 1
        else:
            # Если символ еще не встречался, добавляем его в словарь с начальным значением 1
            char_count_dict[char] = 1

    return char_count_dict


# Пример использования функции
evgene_o = "evgene_o"
result_dict = create_char_count_dict(evgene_o)
print(result_dict)


#4) Чтобы подсчитать количество строчных букв в строке evgene_o, можно использовать словарь, полученный в задаче 3, и проверять каждый символ строки на то, является ли он строчной буквой. Если символ является строчной буквой и присутствует в словаре, увеличиваем счетчик.


def count_lowercase_letters(input_string, char_count_dict):
    # Инициализируем счетчик строчных букв
    lowercase_count = 0
    
    # Проходим по каждому символу строки
    for char in input_string:
        # Проверяем, является ли символ строчной буквой и присутствует ли он в словаре
        if char.islower() and char in char_count_dict:
            lowercase_count += 1

    return lowercase_count


# Пример использования функции с использованием словаря char_count_dict из задачи 3
evgene_o = "evgene_o"
char_count_dict = {'e': 2, 'v': 1, 'g': 1, 'n': 1, '_': 1, 'o': 1}
result = count_lowercase_letters(evgene_o, char_count_dict)
print(result)



#5) Чтобы создать новый словарь dic4, содержащий все пары ключ-значение из словарей dic1, dic2, dic3, можно использовать функцию update() и проходить по каждому словарю, добавляя его элементы в dic4.

def merge_dicts(*dicts):
    # Создаем пустой словарь
    result_dict = {}
    
    # Проходим по каждому словарю
    for dictionary in dicts:
        # Обновляем словарь, добавляя элементы из текущего словаря
        result_dict.update(dictionary)

    return result_dict


# Пример использования функции
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
dic3 = {'e': 5, 'f': 6}
dic4 = merge_dicts(dic1, dic2, dic3)
print(dic4)


# 6) Сумма всех значений из dic4:
sum(dic4.values())


# 7) Произведение всех значений из dic4:
result = 1
for value in dic4.values():
    result = value


# 8) Сумма произведений ключей на их значения в dic4:
sum(key  value for key, value in dic4.items())


# 9) Создание словаря dic7 на базе dic6, но без пар ключ-значение, встречающихся в dic5:
dic7 = {key: value for key, value in dic6.items() if key not in dic5}


# 10) Создание словаря dic8, содержащего все пары ключ-значение
#из dic5 и дополненного парами ключ-значение из dic6, которых нет в dic5:
dic8 = {key: value for key, value in dic5.items()}
dic8.update({key: value for key, value in dic6.items() if key not in dic5})

# 11) Упорядоченный по возрастанию список уникальных значений из ri1:
sorted(list(set(ri1)))


# 12) Создание списка, содержащего последовательность первых и последних значений вложенных списков с сохранением их порядка следования:
result = item[0 for item in nestedlist] + [item[-1] for item in nestedlist]


# 13) Удаление всех пар ключ/значение для символов, встречающихся менее 5 раз в словаре из задачи 3:
dic3 = {key: value for key, value in dic3.items() if value >= 5}



# 14) Программа "мешок":
bag = []
while True:
    value = input("Введите значение или нажмите Enter для выхода: ")
    if not value:
        break
    if value in bag:
        print("Такое значение уже есть в мешке")
    elif len(bag) == 5:
        removedvalue = bag.pop(0)
        print(f"Мешок переполнен. Удалено значение: {removedvalue}")
    bag.append(value)

print("Содержимое мешка:", bag)





