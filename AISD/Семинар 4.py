
# 1.С помощью цикла for сравнить две произвольные строки и вывести строку, состоящую из общих символов исходных строк.
# 

# In[1]:


def common_chars(string1, string2):
    common = ""
    for char in string1:
        if char in string2 and char not in common:
            common += char
    return common

string1 = "hello"
string2 = "world"
result = common_chars(string1, string2)
print(result)


# 2.С помощью цикла while рассчитать двойной факториал для произвольного числа. Двойной факториал n!! числа n рассчитывается как произведение всех чисел, меньших исходного на числа, кратные двум (но это не точно, надо с шагом 2) (вплоть до 1 или 2). Например: 7!! = 7 * 5 * 3 * 1 = 105
# 

# In[4]:


def double_factorial(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

n = 9
r = double_factorial(n)
print(r)


# 3) Решить предыдущую задачу с помощью цикла for

# In[6]:


def double_factorial(n):
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

n = 7
result = double_factorial(n)
print(result)


# 4.Вывести все простые числа в произвольном интервале [a, b], используя вложенные for и конструкцию for-else.

# In[10]:


a = int(input('r'))
b = int(input('g'))
for num in range (a, b+1):
    if i>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
        
    
    


# 5) Реализовать проверку на ввод вводимого пользователем значения: предлагать ввод до тех пор, пока не будет введена непустая строка. Если введено STOP, выводить сообщение "Program interrupted by user". Если введенная строка в лексиграфическом порядке стоит перед строчными латинскими символами, выводить предупреждение "Too early in the dictionary. Try again!" и предлагать ввод снова. Иначе выводить отформатированную исходную строку с заполнителем "_" и шириной 30 символов с выравниванием посередине.

# In[13]:


pl = True
while pl:
    s = input()
    if len() !=0:
        pl = False
        if s == 'STOP':
            print('Program interruped by user')
        elif s[0]<'a':
            print('Too early in the dictionary, Try again')
            pl = True
        else:
            s = s.center(30 + len(s), '_')
            print(s)


# 6) Для произвольной строки вывести те символы, номера которых в строке (не индексы!) делят длину строки без остатка. Для строки "Hello world!" должно выводиться "Hell !".

# In[15]:


x = input()
a = ""
for i, el in enumerate(x):
    if len(x) % (i+1) == 0:
        a += el
         
print(a)


# 7) Даны две произвольные строки. Для всех символов первой строки, которые встречаются во второй строке (без учета регистра), вывести строку: "<номер_символа_в_первой_строке> встречается в строке поиска: <второе_слово>", причем второе слово выводить в нижнем регистре с найденным символом в верхнем регистре. Например, для исходной строки "Hello world!" и строки поиска 'HERD' третья строка в выводе будет содержать текст:
# "9 символ встречается в строке поиска: heRd".
# 
# 

# In[17]:


x = input().lower()
y = input().lower()
k=0
for i in x:
    k+=1
    for j in y:
        if i == j:
            if i == j:
                print(f'{k} встречается в строке поиска:{y.replace(j,j.upper(),1)}')


