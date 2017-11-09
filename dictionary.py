def open_file():
	with open("/usr/share/dict/words", "r") as f:
		dictionary= f.read().split()
		return dictionary

def random_word(dictionary):
	for _ in range(d)
	return dictionary[random.randint(0,len(dictionary))]
