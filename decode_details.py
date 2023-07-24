from Crypto.Cipher import AES
import base64
import os
aes_key = b'Empoweredlmsn0X4TMDKmAHi6alr5paR'

def remove_padding(data):
    # Check for \x07 (bell character) and \x08 (backspace character) as padding
    padding_chars = [b'\x07', b'\x08']
    
    # Loop through each padding character and remove it if found at the end of the data
    for pad_char in padding_chars:
        while data.endswith(pad_char):
            data = data[:-1]
    
    return data
def decrypt_aes_ecb(encrypted_values):
    decrypted_data_dict = {}

    for encrypted_value in encrypted_values:
        encrypted_data = base64.b64decode(encrypted_value)
        cipher = AES.new(aes_key, AES.MODE_ECB)
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_data = remove_padding(decrypted_data)
        decrypted_data_dict[encrypted_value] = decrypted_data.decode('utf-8')

    return decrypted_data_dict

# Replace 'encrypted_value' with the provided encrypted value
# encrypted_value = b'cxafQok5d4qwPcpvnYe4dg=='

# Replace 'aes_key' with the provided AES key in bytes format


# decrypted_value = decrypt_aes_ecb(encrypted_value, aes_key)
# print("Decrypted Value:", decrypted_value)