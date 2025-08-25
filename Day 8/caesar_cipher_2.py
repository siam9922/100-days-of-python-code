#Instructor Notes
#------------------------------------------------------------------------------------------

# TODO-1:
# Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

# TODO-2:
# Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

#  Hint 1 
# You can multiply any number by -1 to make it a negative number.
# TODO-3:
# Combine the encrypt() and decrypt() functions into a single function called caesar().
# Use the value of the user chosen direction variable to determine which functionality to use.
# call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.
#  Hint 2 
# Remember that when you multiply a number by -1 it will reverse its sign. e.g. 3 + ( 5 * -1) is the same as 3 - 5.
#  Hint 3 
# It should say:
# Here is the encoded result: XXX

# or

# Here is the decoded result: XXX


#------------------------------------------------------------------------------------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

