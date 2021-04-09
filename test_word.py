words = open("words.txt", "r")
words = [x.rstrip("\n") for x in words.readlines()]
refwords = open("referencewords.txt", "r")
refwords = [x.strip("\n") for x in refwords.readlines()]
def find_word(word):
	retunrval = False
	if word.lower() in words:
		retunrval = True
	return retunrval


words_needed = []

def main():
	for items in refwords:
		buffer = ""
		for i in items:
			if i != " ":
				buffer += i
		testword = find_word(buffer.lower())
		if testword == False:
			words_needed.append(items.lower())

main()

for i in words_needed:
	print(i)