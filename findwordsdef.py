import os
refwords = open("referencewords.txt", "r")
refwords = [x.strip("\n") for x in refwords.readlines()]

def parser(word):
	buffer = ""
	for i in word:
		if i == " ":
			buffer += "+"
		else:
			buffer += i
	return buffer

for ins in refwords:
	os.system(f"open https://duckduckgo.com/?q={parser(ins)}&ia=web")