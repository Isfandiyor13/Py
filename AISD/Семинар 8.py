
#1) 
l1 = ['1', '123', '123', '12', '1', '123']
print([len(i) for i in l1])

#2)
l1 = ['1', '123', '123', '12', '1', '123']
print(sum(1 for x in l1 if len(x) > 2))

#3) 
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([l2[i] * (l2.index(l2[i]) + 1) for i in range(len(l2))])

#4)
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i for i in l2 if i > 0 ])

#5) 
l2 = [2, 4, -2, -3, 0 , 11 , 3, -1]
print([i if i >= 0 else (l2.index(i) + 1) for i in l2])

#6)
a = input() 
print({char: index + 1 for index, char in enumerate(a)}) 

#7)
lst = [input() for i in range(5)] #пусть длина списка 5
print(sum(1 for c in lst if c in result))

#8)
print({c: "evgene_o".count(c) for c in set("evgene_o")})

#9)
a = ({char: "evgene_o".count(char) for char in set("evgene_o")})
print(sum(value for key, value in a.items() if key.islower()))

#10)
d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sum(key * value for key, value in d4.items()))

#11)
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
print({key: value for key, value in d6.items() if key not in d5})

#12)
d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
print({**d5, **({key: value for key, value in d6.items() if key not in d5})})
