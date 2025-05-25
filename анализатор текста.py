# подготовка текста к анализу

text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

# анализ текста

word_frequency = {}
col = (set(words))
# вывод результатов
print("Количество разных слов:", len(col))
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
