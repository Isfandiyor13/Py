#Семинар 6
#Перечисление:

#1)
numbers = [31, 24, 17]
print(numbers)
numbers_copy = numbers[:]
print(numbers_copy)
numbers_range = list(range(31, 18, -7))
print(numbers_range)
list_of_lists = [numbers, numbers_copy, numbers_range]
print(list_of_lists)


#2.1) 
user_string = input("Введите строку: ")
characters_list = list(user_string)
print(characters_list)

#2.2) 
user_string = input("Введите строку: ")
words_list = user_string.split()
print(words_list)

#2.3) 
user_string = input("Введите строку: ")
digits_list = []
for char in user_string:
    if char.isdigit():
        digits_list.append(char)
print(digits_list)


#3)
my_list = ['input', 'string', 'repeat', 3]
if 'repeat' in my_list:
    repeat_index = my_list.index('repeat')
    repeat_count = my_list[repeat_index + 1]
    new_list = my_list[:repeat_index] + my_list[:repeat_index] * (repeat_count - 1) + my_list[repeat_index:]
    print(new_list)
else:
    print(my_list)


#4)
s1 = "в улучшении качества жизни людей и общества"
s2 = "в сохранении и поддержании природной среды"
output={}
if s1 < s2:
    order = "Строка '{}' идет ПЕРЕД строкой '{}'".format(s1, s2)
else:
    order = "Строка '{}' идет ПОСЛЕ строки '{}'".format(s1, s2)
if output == 'lengths':
    lengths = "Длины строк: {} и {}".format(len(s1), len(s2))
    print(lengths)
elif output == 'order':
    print(order)


#5
max_val = int(input("Введите первое целое число: "))
repeat = int(input("Введите второе целое число: "))

numbers = []
for i in range(1, max_val + 1):
    numbers.extend([i] * repeat)

print(numbers)


#6
max_val = int(input("Введите первое целое число: "))
repeat = int(input("Введите второе целое число: "))

numbers = []
for i in range(1, max_val + 1):
    numbers.extend([i] * repeat)

copy_numbers = numbers.copy()
middle_index = len(copy_numbers) // 2
remove_count = int(len(copy_numbers) * 0.8)
start_index = middle_index - remove_count // 2
end_index = start_index + remove_count

del copy_numbers[start_index:end_index]

for i in range(len(numbers)):
    if numbers[i] not in copy_numbers:
        numbers[i] *= 10

print(numbers)


#7
string = input("Введите произвольную строку: ")
string = string.lower()

result = []
for i in range(len(string)):
    if string[i] == "s" and i != 0 and i != len(string) - 1:
        result.append(string[i-2:i+1])
    else:
        result.append(string[i])

print(result)


#8
string = input("Введите произвольную строку: ")
string = string.lower()

result = []
for i in range(len(string)):
    if string[i] == "s" and i != 0 and i != len(string) - 1:
        result.append(string[i-2:i+1])
    else:
        result.append(string[i])

print(result)

length = int(input("Введите длину списка: "))
user_list = []

for _ in range(length):
    value = input("Введите значение: ")
    if value.isdigit() or '.' in value:
        user_list.append(int(float(value)))
    elif value.lower() == "true":
        
        user_list.append(True)
    elif value.lower() == "false":
        user_list.append(False)
    else:
        user_list.append(value)

print(user_list)

#9
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

words1 = string1.split()
words2 = string2.split()

result = []
for i in range(min(len(words1), len(words2))):
    result.append(words1[i])
    result.append(words2[i])

if len(words1) > len(words2):
    result.extend(words1[len(words2):])
elif len(words2) > len(words1):
    result.extend(words2[len(words1):])

final_string = ' '.join(result)
print(final_string)


#10

string = input("Введите строку: ")
shift = int(input("Введите число слов для сдвига: "))

words = string.split()

shifted_words = words[shift:] + words[:shift]
final_string = ' '.join(shifted_words)
print(final_string)










