user_input = input("Please enter a word: ").upper()

with open("morse_code.txt", "r") as file:
    # Read the text and convert the string representation of the dict into a real dict
    content = file.read()
    # We split at '=' and take the second part to get just the dictionary brackets
    dict_string = content.split("=")[1].strip()
    # Return the string into a dictionary
    morse_dict = eval(dict_string)

# We create one output string for the whole word
encoded_word = ""

for character in user_input:
    if character in morse_dict:
        # Build the Morse string (adding a space between letters)
        encoded_word += morse_dict[character] + " "
print(encoded_word)