letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

encoded_message = "... --- ... / .-- . / .... .- ...- . / .... .. - / .- -. / .. -.-. . -... . .-. --. / .- -. -.. / -. . . -.. / .... . .-.. .--. / --.- ..- .. -.-. -.- .-.. -.--"

def create_dict(letter_to_morse):

    morse_to_letter = {}
    index = 0

    for key, value in letter_to_morse.items():
        morse_to_letter[value] = key

    return morse_to_letter

def decode_message(encoded_message):

    # Create dictionary
    morse_to_letter = {}
    index = 0

    for key, value in letter_to_morse.items():
        morse_to_letter[value] = k

    tokenised_message = encoded_message.split()
    decoded_message = []

    for token in tokenised_message:
        decoded_message.append(morse_to_letter[token])

    decoded = "".join(decoded_message)

    return decoded
