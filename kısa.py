def stutter(word):
	first=word[:2]
	word=f"{first}... {first}... {word}!"
	return word
a=input("Metin Girin")
print(stutter(a))