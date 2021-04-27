textdefs = open("referencewords.txt", "r").readlines()
textdefsfinal = []
deffinitions = []
words = []
# Import words ref
wordsref = open("words.txt", "r").readlines()
wordsreffinal = []
for i in wordsref:
	i = i[0:(len(i) - 2)]
	wordsreffinal.append(i)
	words.append(i)
# Import definitions
deffinistionsimport = open("definitions.txt", "r").readlines()
deffinistionsimportfinal = []
for i in deffinistionsimport:
	i = i[0:(len(i) - 2)]
	deffinitions.append(i)

for i in textdefs:
	textdefsfinal.append(i[0:(len(i) - 2)])

for i in textdefsfinal:
	splited = i.split(":")
	definition = splited[1]
	word = splited[0]
	bufferword = ""
	for i in word.lower():
		if i != " ":
			bufferword += i.lower()
	if bufferword in wordsreffinal:
		continue
	else:
		words.append(bufferword)
		deffinitions.append(definition)

wordswrite = open("words.txt", "w+")
for i in words:
	wordswrite.write(f"{i}\n")

defsswrite = open("definitions.txt", "w+")
for i in deffinitions:
	defsswrite.write(f"{i}\n")