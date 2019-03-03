alphabet = 'abcdefhijklmnopqrstuvwxyz'
key = input('input key that you want to encrypt the message with (1-26): ')
newMessage = ''

message = input('Please Enter your message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_pos = (position + key) % 26
        new_char = alphabet[new_pos]
        newMessage += new_char
    else:
        newMessage += character

print('your new message is: ',newMessage)
