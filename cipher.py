from secrets import choice  
from string import ascii_uppercase


# reads the message file that user inputs
def filereader(filename):
    file = open(filename, "r")
    message = file.read()
    return message

# generates an OTP based on the length of chosen user file
def generate_pad(length):
    finalpad = ""
    for i in range(0,length):
        pad_letter =  choice(ascii_uppercase)
        finalpad += (pad_letter)
    return finalpad   

#reads the generated OTP and creates an array of the ascii values of each letter of the OTP
def shiftamount(OTP):
    pad_ascii_char = []
    for l in OTP:
        lettervalue = ord(l)
        pad_ascii_char.append(lettervalue - 65) 
        # shift = shiftamount(message)
    return pad_ascii_char


def encipher(OTP, message):
    pad_ascii_char = shiftamount (OTP)
    index_pad = 0
    shifted_string = ""
    for j in message:
        char = j
        ascii = ord(char)
        if (ascii >= 65) and (ascii <= 90):
            shifted = (ascii - 65 + pad_ascii_char[index_pad]) % 26 + 65
            shifted_string += chr((shifted))
            index_pad +=1
        elif (ascii >= 97) and (ascii <= 122):
            shifted = (ascii - 97 + pad_ascii_char[index_pad]) % 26 + 97
            shifted_string += chr(shifted)
            index_pad +=1
        else:
          shifted = ascii
          shifted_string += chr(shifted)
    return shifted_string

#debug decipher function
def decipher(OTP, shifted_string):
    pad_ascii_char = shiftamount (OTP)
    index_pad = 0
    deshifted_string = ""
    for j in shifted_string:
        char = j
        ascii = ord(char)
        if (ascii >= 65) and (ascii <= 90):
            deshifted = (ascii - 65 - pad_ascii_char[index_pad]) % 26 + 65
            deshifted_string += chr(deshifted)
            index_pad +=1
        elif (ascii >= 97) and (ascii <= 122):
            deshifted = (ascii - 97 - pad_ascii_char[index_pad]) % 26 + 97
            deshifted_string += chr(deshifted)
            index_pad +=1
        else:
          deshifted = ascii
          deshifted_string += chr(deshifted)
    return deshifted_string

def filewriter(content, filename):
    file = open(filename, "w")
    file.write(content)
    file.close()
    return content, filename

# checks and creates deciphered messaged for encrypted-message.txt
filename = input("Please give me a file name: ") 
precoded_message = filereader(filename)
pad = filereader("pad.txt")
decoded_message = decipher(pad, precoded_message)
filewriter (decoded_message, "decrypted-message.txt")
print ("Decoded message: " + decoded_message)

#WORKING For All Inputs!
# filename = input("Please give me a file name: ") 
# message = filereader(filename)
# OTP = generate_pad(len(message))
# print ("This is your one-time pad: " + OTP)
# encoded_message = encipher(OTP, message)
# print ("Encoded message: " + encoded_message) 
# shifted_string = encoded_message
# decoded_message = decipher(OTP, shifted_string)
# filewriter (decoded_message, "decrypted-message.txt")
# print ("Decoded message: " + decoded_message)


