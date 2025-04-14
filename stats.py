def get_num_words(text):
        words= text.split()
        return len(words)

def count_character_frequency(text):
	character_counts = {}
	for character in text:
		lowercase_character = character.lower()
		if lowercase_character in character_counts:
			character_counts[lowercase_character] +=1
		else:
			character_counts[lowercase_character] = 1
	return character_counts

def sort_character_counts(character_counts):
	chars_list = []
	for char, count in character_counts.items():
		chars_list.append({"char": char, "count": count})

	def sort_on(dict_item):
		return dict_item["count"]
	chars_list.sort(reverse=True, key=sort_on)
	return chars_list
