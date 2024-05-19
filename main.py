def main():
	path_to_book = 'books/frankenstein.txt'
	text = get_book_text(path_to_book)
	word_count = count_words(text)
	letters_count = count_characters(text)
	sorted_values = sort_each_character(letters_count)
	
	print(f"--- Begin report of {path_to_book} ---")
	print(f"{word_count} words found in the document.\n")
	for item in sorted_values:
		print(f"The {item["name"]} character was found {item["num"]} times")
	print("--- End report ---")

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
		elif letter.isalpha():
			counts[letter] = 1
	return counts

def sort_on(dictionary):
	return dictionary["num"]

def sort_each_character(characters_array):
	sorted_by_occurence = []
	for key in characters_array:
		sorted_by_occurence.append({"name": key, "num": characters_array[key]})
	sorted_by_occurence.sort(reverse=True, key=sort_on)
	return sorted_by_occurence


main()