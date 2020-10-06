letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

decoded_message = "SOS We have hit an iceberg and need help quickly"

def encode_message(message):

    temp_encoding = []

    for i in range(len(message)):
        letter = message[i].lower()
        temp_encoding.append(letter_to_morse[letter])

    encoding = "".join(temp_encoding)

    return encoding


encoded_message = "... --- ... / .-- . / .... .- ...- . / .... .. - / .- -. / .. -.-. . -... . .-. --. / .- -. -.. / -. . . -.. / .... . .-.. .--. / --.- ..- .. -.-. -.- .-.. -.--"

# Decoding making use of dictionaries
def create_dict(letter_to_morse):

    morse_to_letter = {}
    index = 0

    for key, value in letter_to_morse.items():
        morse_to_letter[value] = key

    return morse_to_letter

def decode_message(encoded_message):

    tokenised_message = encoded_message.split()
    decoded_message = []

    for token in tokenised_message:
        decoded_message.append(morse_to_letter[token])

    decoded = "".join(decoded_message)

    return decoded

morse_to_letter = create_dict(letter_to_morse)
print(decode_message(encoded_message))

# Decoding making use of functions

def get_key(v):

    for key, value in letter_to_morse.items():
        if(value==v):
            return key

def decode_message(message):

    temp_decoding = []

    tokenised_message = encoded_message.split()

    for token in tokenised_message:
        key = get_key(token)
        # come back to deal with capitalisation
        temp_decoding.append(key)

    decoding = "".join(temp_decoding)

    return decoding
