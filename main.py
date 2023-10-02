text = input("Введите текст: ")
reserved_words = input("Введіть список зарезервованих слів через кому: ").split(',')
words = text.split()
for i in range(len(words)):
    word = words[i].strip('.,?!').lower()
    if word in reserved_words:
        words[i] = words[i].upper()
        new_text = ' '.join(words)
        print("Змінений текст:")
        print(new_text)