STARTING_LETTER_PATH = "Input/Letters/starting_letter.txt"
INVITED_NAMES_PATH = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend/"

PLACEHOLDER_NAME = "[name]"

with open(STARTING_LETTER_PATH, mode="r") as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open(INVITED_NAMES_PATH, mode="r") as invited_names_file:
    invited_names = invited_names_file.read().splitlines()

for name in invited_names:
    letter_name = f"{OUTPUT_PATH}letter_for_{name}.txt"
    letter_text = starting_letter.replace(PLACEHOLDER_NAME, name)
    with open(letter_name, mode="w") as letter:
        letter.write(letter_text)