import random

list_1 = random.sample(range(1, 999), 13)
list_2 = [random.randint(1, 999) for _ in range(13)]

print("списки созданные Random:")
print(list_1)
print(list_2)


def max_element(input_list: list):
    output_list = []
    for key, value in enumerate(input_list):
        if key + 1 < len(input_list) and value < input_list[key + 1]:
            output_list.append(input_list[key + 1])

    return output_list


print("Результат:")
print(max_element(list_1))
print(max_element(list_2))
