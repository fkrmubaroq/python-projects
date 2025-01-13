from art import logo

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', ' ',
              '1', '2', '3', '4', '5', '6', '7', '9', '0',
              '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', '{', ']', ']', ';',
              ':', ',', '<', '>', '.', '/', '?'
              ]

def find_index(search_letter):
    index_letter = 0
    for letter in characters:
        if letter == search_letter:
            break
        index_letter += 1
    return index_letter


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in characters:
            continue

        shift_index = (characters.index(letter) + shift_amount) % len(characters)
        shift_letter = characters[shift_index]
        cipher_text += shift_letter
    return cipher_text


def decrypt(cipher_text, shift_amount):
    return encrypt(cipher_text, -shift_amount)


def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode != "encode" and encode_or_decode != "decode":
        return "unknown"

    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        shift_index = (characters.index(letter) + shift_amount) % len(characters)
        shift_letter = characters[shift_index]
        output_text += shift_letter

    return output_text


should_continue = True

print(logo)
while should_continue:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encode_text = caesar(text, shift, "encode")
    decode_text = caesar(encode_text, shift, "decode")
    print(f"Encode : {encode_text}")
    print(f"Decode : {decode_text}")

    restart = input("Type 'yes' if you want to go again, Otherwise, type 'no : ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye~")

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
