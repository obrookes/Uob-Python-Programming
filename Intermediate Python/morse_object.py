""" A Morse Encode-Decoder Class """

class MorseTranslator:

    def __init__(self):

        self._letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                           'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                           'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                           'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                           '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                           '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                           ' ':'/' }

        self._morse_to_letter = {}

        for letter in self._letter_to_morse:
            morse = self._letter_to_morse[letter]
            self._morse_to_letter[morse] = letter

    def encoder(self, message):
        """ Takes a string as input and encodes as morse """
        temp_encoding = []
        for i in range(len(message)):
            letter = message[i].lower()
            temp_encoding.append(self._letter_to_morse[letter])

        encoding = " ".join(temp_encoding)
        return encoding

    def decoder(self, message):
        """ Takes morse code as input and decodes as string """

        tokenised_message = message.split(" ")
        decoded_message = []

        for token in tokenised_message:
            decoded_message.append(self._morse_to_letter[token])

        decoded = "".join(decoded_message)
        return decoded
