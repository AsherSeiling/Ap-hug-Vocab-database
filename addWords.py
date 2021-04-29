refwords = open("referencewords.txt", "r")
refwords = [x.strip("\n") for x in refwords.readlines()]
words = []
definitions = []
deffinitionsfile = open("definitions.txt", "r")
definitions = [x.strip("\n") for x in deffinitionsfile.readlines()]
wordsfile = open("words.txt", "r")
words = [x.strip("\n") for x in wordsfile.readlines()]

for i in refwords:
	i = i.split(": ")
	word = i[0]
	wordbuffer = ""
	for x in word.lower():
		if x != " ":
			wordbuffer += x.lower()
	word = wordbuffer
	deffinition = i[1]
	words.append(word)
	definitions.append(deffinition)

opendefwrite = open("definitions.txt", "w+")
openwordwrite = open("words.txt", "w+")
for i in definitions:
	opendefwrite.write(f"{i}\n")
for i in words:
	openwordwrite.write(f"{i}\n")