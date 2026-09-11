import Morse_Dict as MD

user_text = input("Enter the text you wish to convert to Morse :\n").lower()

morse_text = ""

for letter in user_text:
    if letter in MD.Morse_Code_Dict:
        morse_text += MD.Morse_Code_Dict[letter]
        
print(f"Text : {user_text}\nMorse : {morse_text}")
