
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caeser(direction, text, shift):            
        if direction == 'encode': # encryption function
            def encrypt(original_text = text, shift_amount = shift):
                encrypted_text = ""
                for letter in original_text:
                    if letter in alphabet:
                        position = alphabet.index(letter)
                        new_position = position + shift_amount                 
                        if new_position > 25:
                            new_position %= len(alphabet)
                            encrypted_text += alphabet[new_position]
                        else:
                            encrypted_text += alphabet[new_position]
                    else:
                        encrypted_text += letter 
                print(f"The encoded text is : {encrypted_text}")
            encrypt(text, shift)
        elif direction == 'decode': # decryption function
            def decrypt(original_text = text, shift_amount = shift):
                decrypted_text = ""
                for letter in original_text:
                    if letter in alphabet:
                        position = alphabet.index(letter)
                        new_position = position - shift_amount                 
                        if new_position < 0:
                            new_position %= len(alphabet)
                            decrypted_text += alphabet[new_position]
                        else:
                            decrypted_text += alphabet[new_position]
                    else:
                        decrypted_text += letter 
                print(f"The decoded text is : {decrypted_text}")                
            decrypt(text, shift)
        else:
            print("Invalid direction. Please type 'encode' or 'decode'")

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
        
    caeser(direction, text, shift)

    restart = input("\n********************Do you want to continue?. Type 'yes' to continue or 'no' to exit********************\n").lower()
    if restart == "no" or restart != "yes":
        end = True
        print("\nThank you for using the Caesar Cipher program. Goodbye!")