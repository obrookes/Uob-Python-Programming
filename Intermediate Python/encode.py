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
