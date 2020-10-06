import sys

letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

morse_to_letter = {}

for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter

def encode_message(message):
    """ Takes a string as input and encodes as morse """
    temp_encoding = []
    for i in range(len(message)):
        letter = message[i].lower()
        temp_encoding.append(letter_to_morse[letter])

    encoding = " ".join(temp_encoding)
    return encoding

def decode_message(message):
    """ Takes morse code as input and decodes as string """
    tokenised_message = message.split()
    decoded_message = []

    for token in tokenised_message:
        decoded_message.append(morse_to_letter[token])

    decoded = "".join(decoded_message)
    return decoded

if __name__ == "__main__":
    # Don't run this code if this script is being
    # imported as a module

    from morse_object import MorseTranslator
    translator = MorseTranslator()
    message="Hello World"
    print(translator.decoder(translator.encoder(message)) == message)


    help(encode_message)
    print("Hello World")
