first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая часть задачи
first_result = [len(string) for string in first_strings if len(string) >= 5]

# Вторая часть задачи
second_result = [(first_word, second_word) for first_word in first_strings for second_word in second_strings if len(first_word) == len(second_word)]

# Третья часть задачи
combined_strings = first_strings + second_strings
third_result = {string: len(string) for string in combined_strings if len(string) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)

