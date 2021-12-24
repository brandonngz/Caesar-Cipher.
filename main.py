from art import logo
import ansi_code as ansi
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    cipher_list = []
    for char in range(len(text)):
        if ' ' in text[char]: cipher_list += ' '
        elif text[char] not in alphabet: cipher_list += text[char]
        else:
            letter_position = alphabet.index(text[char])
            if direction == "encode":
                shifted_index = (letter_position + shift) % 26
            elif direction == "decode":
                shifted_index = (letter_position - shift) % 26
            cipher_list += alphabet[shifted_index]    
    print(f"The {direction}d text is {''.join(cipher_list)}")
    
# Cool logo with ANSI color makes it cooler =) 
print(f'{ansi.fgRed}{logo}{ansi.reset}')

while True:
    direction = input(f"Type {ansi.fgRed}'encode'{ansi.reset} to encrypt, type {ansi.fgBlue}'decode'{ansi.reset} to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    print("<----------------------------------->")
    close = input("Do you wanna keep encoding? Yes or No \n").lower()
    if close == "no":
        print("Thanks by decoding with me =)")
        break
