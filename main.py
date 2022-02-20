import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

# Dictionary comprehension
new_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
is_word_crt = True
while is_word_crt:
    try:
        # Create a list of words from the above dict based on letters when user inputs a word
        user_input = input("Enter a word: ").upper()
        # Check for word in dict based on each letter extracted and get it to a list
        result = [new_dict[k] for k in user_input]
        print(result)
        is_word_crt = False
    except KeyError:
        print('Invalid word. Please enter a valid word')
