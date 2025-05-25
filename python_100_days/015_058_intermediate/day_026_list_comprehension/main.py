import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        word_to_nato = [nato_dict[letter] for letter in user_word]       
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(word_to_nato)

generate_phonetic()
