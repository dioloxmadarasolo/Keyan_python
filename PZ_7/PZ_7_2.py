# Дана строка-предложение на русском языке. Вывести самое короткое слово в
# предложении. Если таких слов несколько, то вывести последнее из них. Словом
# считать набор символов, не содержащий пробелов, знаков препинания и
# ограниченный пробелами, знаками препинания или началом/концом строки.


sentence = "строка предложение на русском языке"

words = sentence.split()

filtered_words = [word.strip(".,!?;:") for word in words]

lengths = [len(word) for word in filtered_words]

min_length = min(lengths)

shortest_index = lengths.index(min_length)

print(filtered_words[shortest_index])