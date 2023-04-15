WORD={}
lengths=[]

text = input("Text: ")
phrases = text.split(" ")
for text in phrases:
    if text in WORD.keys():
        WORD[text] += 1
    else:
        WORD[text] = 1

list_words = WORD.keys()
sorted_words = sorted(list_words)

for phrases in WORD.keys():
    length = len(phrases)
    lengths.append(length)
    width = max(lengths)

for text in sorted_words:
    print(f"{text:<{width}}: {WORD[text]}")