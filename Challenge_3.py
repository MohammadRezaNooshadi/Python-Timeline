"""
Challenge 3: Multi-Format Text & Keyword Analyzer
Write a Python script that collects multi-line text input from the user and performs advanced word frequency and string analysis using custom functions.

Requirements:
1. Multi-line Input Collection:

    Continuously prompt the user to enter lines of text until they type 'END' on a new line to finish.

2. Custom Function — clean_and_tokenize(raw_text):

    Write a function that accepts the raw text string.
    Strip punctuation marks (e.g., ., ,, !, ?), convert the text to lowercase, and split it into a list of individual words.

3. Custom Function — build_frequency_map(words_list):

    Write a function that accepts the words list and returns a dictionary (dict) where keys are unique words and values are their occurrence counts.

4. Analysis & Report:

    Filter out words with a length of less than 3 characters from the final dictionary.
    Identify and display the most frequent word and the longest word entered.
    Display the final word counts in a clean, formatted structure.
    Use an if check to handle empty text input gracefully without crashing.
"""
#define a storage list for every line
txt = []

print("inter your text below(type '/s' on newline when you done):\n")
#define a loop to get all the text
while True:
    line = input("...")
    #stop condition
    if line == "/s":
        break
        #store every line in list
    txt.append(line)