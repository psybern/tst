import re

with open('txt.txt', 'r+', encoding='utf-8') as list_1:
    text_1 = list_1.read()

    list_2 = re.sub(r"[\([{«,.'':;—»})\]0-9*#%^]", "", text_1)
    list_3 = list_2.lower()
    list_4 = list_3.split()

    print(len(list_4))
    print(len(set(list_4)))

