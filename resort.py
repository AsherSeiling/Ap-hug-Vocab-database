words = open("words.txt", "r")
definitions = open("definitions.txt", "r")
words = [x.rstrip("\n") for x in words.readlines()]
definitions = [x.rstrip("\n") for x in definitions.readlines()]

definitions_ref = []
definitions_indexed = []
words_sorted = []
for i in words:
    words_sorted.append(i)

for i in words:
    definitions_ref.append(words.index(i))

words.sort()
for i in words:
    definitions_indexed.append(words_sorted.index(i))


finished_def = []
finished_word = []

for i in definitions_indexed:
    finished_word.append(words_sorted[i])
    finished_def.append(definitions[i])

for i in finished_word:
    print(i)
print("\n\n\n")
for i in finished_def:
    print(i)
