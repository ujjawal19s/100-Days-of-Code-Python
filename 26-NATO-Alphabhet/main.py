import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name? ").upper()

letter_list = [letter for letter in name]

word_list = [nato_dict[char] for char in letter_list]

print(word_list)
