from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
re_run = True
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    


while re_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":

        text = input("Type your message:\n").lower()

        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Please type a valid shift number!")
        else:
            shift = shift % 26
            caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
            go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

            if go_again == "no":
                re_run = False

    else:
        print("Please type 'encode' or 'decode'.")
