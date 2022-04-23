import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True


def cipher(plain_text, shift_amount, direction_cipher):
    cipher_text = ''
    for letter in plain_text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            if direction_cipher == 'encode':
                new_position = letter_position + shift_amount
                cipher_text += alphabet[new_position]
            if direction_cipher == 'decode':
                new_position = letter_position - shift
                cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f'the text is {cipher_text}')


while should_continue:
    direction = input("type 'encode' to encrypt. type 'decode' to decrypt \n").lower()
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number: \n'))

    shift = shift % 26
    cipher(text, shift, direction)

    again = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if again == 'yes':
        pass
    elif again == 'no':
        should_continue = False
        print('GoodBye')
