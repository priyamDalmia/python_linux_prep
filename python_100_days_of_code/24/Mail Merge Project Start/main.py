#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os 
from pathlib import Path
import copy 


parent_dir = Path(__file__).parent 
input_dir = parent_dir / "Input"
if not input_dir.exists():
    raise Exception("Input dir not found!")
example_file = input_dir / "Letters" / "starting_letter.txt"
with example_file.open(mode='r') as file:
    lines = file.readlines()

names_file = input_dir / "Names" / "invited_names.txt"
with names_file.open(mode='r') as file:
    all_names = file.readlines()

output_dir = parent_dir / 'Output' / 'ReadyToSend'
for name in all_names:
    name = name.strip()
    letter_path = output_dir / f'{name}.txt'
    letter_text = copy.copy(lines)
    letter_text[0] = letter_text[0].replace('[name]', name)
    if not letter_path.exists():
        with letter_path.open('+w') as file:
            file.writelines(letter_text)

if __name__ == "__main__":
    pass