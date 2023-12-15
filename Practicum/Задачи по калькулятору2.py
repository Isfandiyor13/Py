
def fractional_part(a, b):
    quotient = a // b  # Целая часть
    remainder = a % b  # Остаток

    fraction = ""  # Дробная часть
    decimal_places = 6  # Количество знаков после запятой

    # Пока есть остаток и не достигнуто нужное количество знаков после запятой
    while remainder != 0 and len(fraction) < decimal_places:
        # Делим на 10 и получаем новый остаток
        remainder *= 10
        quotient = remainder // b
        remainder %= b

        fraction += str(quotient)

    # Если периодическая часть существует
    if remainder != 0:
        # Находим периодическую часть
        period = find_period(fraction)
        if period != "":
            return f"{quotient}.{fraction[:decimal_places]} и {period} в периоде"
        else:
            return f"{quotient}.{fraction[:decimal_places]}"

    return f"{quotient}.{fraction[:decimal_places]}"

# Функция для нахождения периодической части строки
def find_period(string):
    n = len(string)
    for i in range(1, n // 2 + 1):
        period = string[:i]
        if string.startswith(period * (n // i)):
            return period

    return ""

# Пример использования
result = fractional_part(19, 99)
print(result)
