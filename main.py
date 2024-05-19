def main():
	path_to_book = 'books/frankenstein.txt'
	text = get_book_text(path_to_book)
	word_count = count_words(text)
	letters_count = count_characters(text)
	print(f"{word_count} words found in the document.")
	print(f"Unique letters: {letters_count}")

def count_words(text):
	return len(text.split())

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_characters(text):
	counts = {}
	for letter in text.lower():
		if letter in counts:
			counts[letter] += 1
		else:
			counts[letter] = 1
	return counts

main()