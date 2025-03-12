# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

import pandas
# {new_key:new_value for (index,row) in df.iterrows()}

# create a data frame based on the csv "nato_phonetic_alphabet.csv"
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# use .itterows() to iterate over the data frame in order to create a dictionary in the following format
# {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter:row.code for (index,row) in df.iterrows()}

# collect user input
user_input = input("Type a word:\n").upper()

# convert the user input word into a NATO alphabetically accurate word
coded_word = [new_dict[letter] for letter in user_input]
print(coded_word)
