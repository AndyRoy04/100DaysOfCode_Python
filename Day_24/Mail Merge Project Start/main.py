starting_letter_path = '100DaysOfCode_Python/Day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt'
invited_names_path = '100DaysOfCode_Python/Day_24/Mail Merge Project Start/Input/Names/invited_names.txt'
output_path = '100DaysOfCode_Python/Day_24/Mail Merge Project Start/Output/ReadyToSend/'

with open(invited_names_path) as invited_names:
    names = invited_names.readlines()

# new_name_list = [name[:-1] for name in names] 
# # The name[:-1] takes each name in the list and 
# removes the 2 last characters i.e \n

with open(starting_letter_path) as starting_letter:
    letter = starting_letter.read()

for name in names:
    stripped_name = name.strip() # this takes out the any white spaces in the text file
    new_letter = letter.replace('[name]', stripped_name)
    with open(f'{output_path}/letter_for_{stripped_name}.docx', 'w') as Output:
        Output.write(new_letter)  # This will write the new letter to the output file.


# Day 24 of #100DaysOfCode
# Today I had to build a Mail Merge program to merge the two files together and send them to the server in the same folder 


