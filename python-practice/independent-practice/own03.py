sentence = "the cat sat on the mat the cat"
my_dict = {}
for word in sentence.split():
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
for word, times in my_dict.items():
    if times >= 2:
        print(f"{word}:{times}")
