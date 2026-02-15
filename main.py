import os # Standard library for file/folder operations

user_input = input("Please enter a word: ").upper()

# Check if the directory exists; if not, create it
if not os.path.exists("morse_code_output"):
    os.makedirs("morse_code_output")

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

# Save the result to a file named after the input word
# Make sure the folder 'morse_code_output' actually exists!
with open(f"morse_code_output/{user_input}.txt", "w") as file:
    file.write(encoded_word)
    print(f"File saved successfully for: {user_input} = {encoded_word}")