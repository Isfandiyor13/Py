l1 = ['1', '123', '123', '12', '1', '123']
l2 = [2, 4, -2, -3, 0 , 11 , 3 -1]
d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}

#4.13)
new_l1 = [len(x) for x in l1]
print(new_l1)

#4.14) 
count = sum(1 for x in l1 if len(x) > 2)
print(count)

#4.15) 
result = sum(k * v for k, v in d4.items())
print(result)

#4.16) 
d7 = {k: v for k, v in d6.items() if k not in d5}
print(d7)

#4.17)
new_l2 = [(i + 1) * v if v is not None and i is not None else v for i, v in enumerate(l2)]
print(new_l2)

#4.18)
new_l2 = [x for x in l2 if x >= 0]
print(new_l2)

#4.19)
new_l2 = [i + 1 if x < 0 else x for i, x in enumerate(l2)]
print(new_l2)

#5.1)
factor1 = input()
factor2 = input()
product = float(factor1) * float(factor2)
print(f'{factor1} умножить на {factor2} будет: {product}')

#5.2)
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(2,4,7))

#5.3)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Деление на ноль невозможно, это вам не пределы"
print(add(6,3))


#5.6)
def calc(expression):
    num1, op, num2=expression.split()
    num1=int(num1)
    num2=int(num2)
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1//num2
    elif op=='%':
        return num1%num2  
    elif op=='^':
        return num1**num2  
print(calc(input('Введите строковое выражение вида <число> <операция> <число>')))


#5.7)
def print_car_info(brand='Audi', model='A7', color='синий', year=2010, mileage=215000, license_plate='X012АМ77', price=20000):
    print(f"Автомобиль марки: {brand}, модели: {model}, цвета: {color}, {year} года выпуска, с пробегом: {mileage} км, c номерным знаком: {license_plate}, цена: {price} руб.")
    
c1={'brand': 'Opel', 'model': 'astra', 'color': ',белый', 'mileage': 180000, 'price': 7700}
c2={'brand': 'Toyota', 'model': 'RAV4', 'color': 'серебристый', 'year': 2015, 'price': 1200000}

print_car_info(**c1)
print_car_info(**c2)


#5.8)
def to_text(num):
    numbers_map = {
        0: 'Ноль', 1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 5: 'Пять', 6: 'Шесть', 7: 'Семь', 8: 'Восемь', 9: 'Девять',
        10: 'Десять', 11: 'Одиннадцать', 12: 'Двенадцать', 13: 'Тринадцать', 14: 'Четырнадцать', 15: 'Пятнадцать',
        16: 'Шестнадцать', 17: 'Семнадцать', 18: 'Восемнадцать', 19: 'Девятнадцать', 20: 'Двадцать', 30: 'Тридцать',
        40: 'Сорок', 50: 'Пятьдесят', 60: 'Шестьдесят', 70: 'Семьдесят', 80: 'Восемьдесят', 90: 'Девяносто'
    }
    
    if num in numbers_map:
        return numbers_map[num]
    else:
        tens = num // 10 * 10
        ones = num % 10
        return f"{numbers_map[tens]} {numbers_map[ones].lower()}"

print(to_text(15))  


#5.9)
def to_int(text):
    numbers_map = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
        'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
        'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30,
        'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90
    }
    
    parts = text.split()
    number = 0
    for part in parts:
        if part in numbers_map:
            number += numbers_map[part]
    
    return number

print(to_int('тридцать три')) 



