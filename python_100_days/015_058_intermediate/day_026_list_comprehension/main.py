import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()
word_to_nato = [nato_dict[letter] for letter in user_word]
print(word_to_nato)
