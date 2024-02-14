import art

print(art.logo)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(raw_text, shift_amount, main_direction):
    end_text = ""  
    if main_direction == "decode":
        shift_amount *= -1
    for letter in raw_text:
        if letter in alphabet:
            position  = alphabet.index(letter)                  #  .index() gives the index position in list
            new_position =position + shift_amount
            new_position %= 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {main_direction}d text is  : {end_text}")
    
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to Encrypt or Type 'Decode' to Decrypt: \n ")
    text = input("Type your message: ").lower()
    shift = int(input("Type Shift value: "))
    
    caesar(raw_text = text, shift_amount= shift, main_direction = direction )   

    instruct = input("Type'YES' if you want to go again or Type 'NO' to stop.\n").lower()
    if instruct == "no":
        should_continue = False
        print("GoodBye!")