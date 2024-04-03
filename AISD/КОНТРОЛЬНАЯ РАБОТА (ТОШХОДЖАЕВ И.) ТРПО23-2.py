#!/usr/bin/env python
# coding: utf-8

# ### Контрольная работа № 1.
# ### Вариант 2.
# #### Студент  Тошходжаев Исфандиер   ( группа ) ТРПО23-2 

# 1. Напишите программу, которая выполняет добавление, удаление и вывод на экран элементов списка при помощи классов. 
# 
# Решение задачи
# 
# 1.	Создаем класс и с помощью конструктора инициализируем значения этого класса.
# 2.	Создаем в данном классе методы для добавления, удаления и вывода на экран соответствующих значений.
# 3.	Создаем объект данного класса.
# 4.	Используя созданный объект, вызываем соответствующий метод (в зависимости от выбора пользователя).
# 5.	Выводим результат на экран.
# 6.	Конец.
# 
# В программе реализовать выбор с помощью меню:
# 
# print("0. Выход")
# 
# print("1. Добавить")
# 
# print("2. Удалить")
# 
# print("3. Вывести на экран")
# 
# choice = int(input("Выберите одно из этих значений: "))
# 
# 

# In[ ]:


# Решение 1.
class MyList:
    def __init__(self):
        self.my_list = []
    
    def add_element(self, element):
        self.my_list.append(element)
    
    def remove_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
    
    def display_elements(self):
        for elem in self.my_list:
            print(elem)

my_list_obj = MyList()

while True:
    print("0. Выход")
    print("1. Добавить")
    print("2. Удалить")
    print("3. Вывести на экран")
    
    choice = int(input("Выберите одно из этих значений: "))
    
    if choice == 0:
        print("Программа завершена.")
        break
    elif choice == 1:
        element = input("Введите элемент для добавления: ")
        my_list_obj.add_element(element)
    elif choice == 2:
        element = input("Введите элемент для удаления: ")
        my_list_obj.remove_element(element)
    elif choice == 3:
        my_list_obj.display_elements()
    else:
        print("Недопустимый выбор. Попробуйте снова.")


# 2. Используя класс People в качестве базового, создайте класс Сотрудник (Worker), имеющий свойства:
# 
# • должность (post)
# 
# • зарплата (salary)
# 
# методы:
# 
# • __init__ – конструктор;
# 
# • __str__ – аналогично методу класса Teacher из примера.
# 
# Используя класс Сотрудник в качестве базового создайте класс Преподаватель (Teacher), имеющий:
# 
# • закрытый атрибут дисциплины (disciplines), в котором хранятся названия дисциплин, которые ведет преподаватель;
# 
# • методы __init__ и __str__;
# 
# • методы добавить_дисциплину (add_dis) и удалить_дисциплину (delete_dis), которые позволяют изменять список дисциплин.
# 
# Создайте список, содержащий по 2 объекта каждого класса (People, Worker, Teacher). Для этого списка:
# 
# • выведите информацию о каждом человеке с помощью метода info;
# 
# • выведите фамилии тех, кто моложе 30 лет;
# 
# • продемонстрируйте работу со свойствами должность и зарплата и методами добавить_дисциплину и удалить_дисциплину.
# 

# In[9]:


# Решение 2.
class People:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def info(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}"
    
class Worker(People):
    def __init__(self, first_name, last_name, age, post, salary):
        super().__init__(first_name, last_name, age)
        self.post = post
        self.salary = salary
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Post: {self.post}, Salary: {self.salary}"
    
class Teacher(Worker):
    def __init__(self, first_name, last_name, age, post, salary, disciplines=None):
        super().__init__(first_name, last_name, age, post, salary)
        self.__disciplines = disciplines if disciplines is not None else []
    
    def add_dis(self, discipline):
        self.__disciplines.append(discipline)
    
    def delete_dis(self, discipline):
        if discipline in self.__disciplines:
            self.__disciplines.remove(discipline)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Post: {self.post}, Salary: {self.salary}, Disciplines: {', '.join(self.__disciplines)}"

# Создаем объекты
people1 = People("John", "Doe", 25)
people2 = People("Alice", "Smith", 35)

worker1 = Worker("Bob", "Johnson", 28, "Manager", 50000)
worker2 = Worker("Emma", "Brown", 40, "Engineer", 60000)

teacher1 = Teacher("Mark", "Davis", 30, "Teacher", 45000, ["Math", "Physics"])
teacher2 = Teacher("Sarah", "Wilson", 29, "Instructor", 48000, ["English", "History"])

people_list = [people1, people2, worker1, worker2, teacher1, teacher2]

# Выводим информацию о каждом человеке
for person in people_list:
    print(person.info())

# Выводим фамилии тех, кто моложе 30 лет
for person in people_list:
    if person.age < 30:
        print(person.last_name)

# Демонстрируем работу со свойствами и методами Teacher
print(teacher1)
teacher1.add_dis("Chemistry")
print(teacher1)
teacher1.delete_dis("Physics")
print(teacher1)


# 3.Создайте класс Заказ(Order), у которого есть свойства кодтовара(code), цена(price), количество(count) и методы _init и str.
# 
# Создайте 2 класса-потомка: Опт(Opt) и Розница(Retail). В этих классах создайте методы init, str.и сумма_заказа(summa), позволяющий узнать стоимость заказа. Для опта стоимость единицы товара составляет 95% от цены, а при покупке более 500 штук – 90% цены. В розницу стоимость единицы товара составляет 100% цены. Стоимость заказа равна произведению цены на количество.
# 
# Продемонстрируйте работу с классами, создав необходимые объекты и обратившись к их свойствам и методам

# In[6]:


# Решение 3.

class Order:
    def __init__(self, code, price, count): #добавляем свойства:
        self.code = code
        self.price = price
        self.count = count
    
    def __str__(self):
        return f"Order: {self.code}, Price: {self.price}, Count: {self.count}"

class Opt(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)
    
    def summa(self):
        if self.count > 500:
            return self.price * self.count * 0.9
        else:
            return self.price * self.count * 0.95
    
    def __str__(self):
        return f"Opt Order: {self.code}, Total Price: {self.summa()}"

class Retail(Order):
    def __init__(self, code, price, count):
        super().__init__(code, price, count)
    
    def summa(self):
        return self.price * self.count
    
    def __str__(self):
        return f"Retail Order: {self.code}, Total Price: {self.summa()}"

# Создаем объекты
order1 = Opt("A001", 100, 600)
order2 = Retail("B002", 50, 10)

# Выводим информацию о заказах
print(order1)
print(order2)

# Выводим стоимость заказов
print(order1.summa())
print(order2.summa())


# 4.Написать функцию-генератор my_func_2(lst), которая принимает объект, поддерживающий итерации с произвольным уровнем вложенности, и возвращает все элементы по одному.

# In[4]:


# Решение 4.
def myfunc2(lst):
    if isinstance(lst, (list, tuple, set)):
        for item in lst:
            yield from myfunc2(item)
    else:
        yield lst

# Пример использования
nestedlist = [[[2, 4], [6, 7]], [[9, 8]]]
for item in myfunc2(nestedlist):
    print(item)


# 5.С помощью механизма map/filter/reduce (хотя бы одна из этих функций должна быть использована в решении) посчитать в тексте количество слов, состоящих не менее, чем из 3-х букв. Слова в тексте разделены пробелами. Написать реализацию в одну строку. Оформить решение в виде функции my_func_3(text), т.е. шаблон таков:
# 
# строка с import, если необходимо def my_func_3(text): return # однострочная реализация задания

# In[7]:


# Решение 5.
import functools

def my_func_3(text):
    return functools.reduce(lambda x, y: x + y, map(lambda word: 1 if len(word) >= 3 else 0, text.split()))

# Пример использования
text = "This is a sample text with some words of different lengths"
print(my_func_3(text))


# In[ ]:




