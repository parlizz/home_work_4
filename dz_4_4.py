from random import randint

list_2 = [randint(1, 99) for i in range(14)]
print(f'случайны список из 14 элементов: {list_2}')

new_list = [i for i in list_2 if list_2.count(i) < 2]

print(f'проверочный список: {new_list}')
