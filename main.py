import sys
from stats import get_num_words, count_character_frequency, sort_character_counts

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	text = get_book_text(path)
	num_words = get_num_words(text)
	character_count = count_character_frequency(text)
	sorted_characters = sort_character_counts(character_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count -----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for item in sorted_characters:
        	char = item["char"]
       		count = item["count"]
       		if char.isalpha():
           		print(f"{char}: {count}")

	print("============= END ===============")

main()
