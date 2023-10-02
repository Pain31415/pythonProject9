text = input("Введіть текст: ")
num_sentences = text.count('.') + text.count('!') + text.count('?')
print("Кількість речень: ", num_sentences)