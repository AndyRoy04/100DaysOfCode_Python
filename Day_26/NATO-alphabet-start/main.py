import pandas

file_path = '100DaysOfCode_Python/Day_26/NATO-alphabet-start/nato_phonetic_alphabet.csv'
phonetics_data = pandas.read_csv(file_path)
# print(phonetics_data)

# #TODO 1. Create a dictionary in this format:
phonetics_dict = {row.letter:row.code for index, row in phonetics_data.iterrows()}
# print(phonetics_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter a word: ').upper()
user_word_list = [phonetics_dict[letter] for letter in user_word if letter in phonetics_dict]
print(user_word_list)
