text = input('Enter the text you want to encrypt: ')
password = input('Enter the password: ')
encrypted_text = '' 
for char in text:
    encrypted_char = chr(ord(char) + len(password))
    encrypted_text += encrypted_char
print('Encrypted text:', encrypted_text)

decrypt = input('Do you want to decrypt the text? (yes/no): ')

if decrypt == 'yes':
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = chr(ord(char) - len(password))
        decrypted_text += decrypted_char

    print('Decrypted text:', decrypted_text)


