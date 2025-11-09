"""A simple dictionary application that retrieves word meanings from a JSON file."""

#Loads a json file
from json import load
#Finds close matches to a word
from difflib import get_close_matches

#Load the dictionary data from a JSON file
data = load(open("source.json"))

def mean_word(word = "dictionary"):
	"""Returns the meaning of a word or suggests a close match if the word is not found."""
	try:
		return data[word.lower()]
	except KeyError:
		similar_words = get_close_matches(word, data.keys())
		if similar_words:
			closest_match = similar_words[0]
			confirmation = input(f"Did you mean '{closest_match}' instead of '{word}'? Enter Y if yes, or N if no: ")
			if confirmation.lower() == 'y':
				return data[closest_match]
			else:
				return ["The word doesn't exist. Please double-check it."]
		else:
			return ["The word doesn't exist. Please double-check it."]

meaning = mean_word(input("Enter a word: "))

for mean in meaning:
	print(mean)
