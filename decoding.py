

# # Example usage

import jwt
from decode_details import decrypt_aes_ecb
# Replace 'your_access_token' with the actual JWT access token you have
access_token = b'eyJhbGciOiJSUzI1NiIsImtpZCI6IlYwRURKTklFUkk4WkpOSkRBUlIxUEdQWUFaRFVHLTBWRUhYR1hfVEoiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJjUXhKdlhuUmovMm1IREVPV1FWOVpRPT0iLCJuYW1lIjoiY3hhZlFvazVkNHF3UGNwdm5ZZTRkZz09Iiwicm9sZSI6IkNBIiwidXNlcm5hbWUiOiJmazJ6dUdudVEvbEoyQnkrUEx2TlRnPT0iLCJhZGRyZXNzIjoiMDlxaUdtNThaR3d3U3VWK1lCcTlZRnFjSXFCVTBqQzNET2pjOVhNOWw1VTB6ZnJ4TWJmcysya0lJZzFCMmQwTUtGaUxveW13WnhweHhDSUNKU3puS0VKMjRkVVV0VkF1TW8zUi9DUTdQd1g0cGNMcncyaHNPR0dTTWV2Mk12VnkiLCJsb2NhbGl0eSI6IjBxNFVXVlBzUFJGZXJESlYrSzdYdGc9PSIsInBlcm1pc3Npb25zIjoiY3RtIHNjIHVjIHJhcyBydWwgcmN3YyByY2NzIHJ1YSByZnMgdWxzdCB1ZnIgZGNvbmYgcnAgcmx1dSBybHUgdGQgY2EgbWQgc2Mgem0gY3AgZXRtIHNtYyBsY21zIGN0bSBjbSB1bSBmcSBhcSBvcHIgaWFxZCBseWNvIGljYXBwIHJsIGNyciBhY3RjZmcgdWxyIHVubCBlX2NmIHNtc19jIHJjYSIsInN1YnNpZGlhcnkiOiItIiwidGhlbWUiOiJ3aGl0ZSIsImxvZ29uYW1lIjoiYXNzZXRzXFxpbWdcXG5pc21cXDYzODI0OTU1MzY0NjU5NTYyME5JU01Mb2dvLnBuZyIsImxvZ29uYW1lZGFyayI6ImFzc2V0c1xcaW1nXFx0YXRhbW90b3JzXFw2MzgyMDM0MzkzNzQ1OTg0NTgyMTB4NTVfZGFyay5wbmciLCJpc2luc3RpdHV0ZSI6IkZhbHNlIiwic3RhdHVzY29kZSI6Ii0iLCJzdGF0dXNjb2RlbWVzc2FnZSI6Ii0iLCJpb3MiOiItIiwibGRhcCI6IjAiLCJleHRfdXNlciI6IjAiLCJmY210b2tlbiI6Ii0iLCJ0b2tlbl91c2FnZSI6ImFjY2Vzc190b2tlbiIsImp0aSI6IjIwZjcwMGI1LTZiZjgtNGU5Mi1hNjk5LTU3ZjAyMTBiYjAxOSIsImF1ZCI6WyJtYXN0ZXJzLWFwaSIsImxvZ2dpbmctYXBpIiwiY29uZmlndXJhdGlvbi1hcGkiLCJ1c2Vycy1hcGkiLCJjb3Vyc2UtYXBpIiwiYXNzZXNzbWVudF9hcGkiLCJiaWxsaW5nX2FwaSIsImNlcnRpZmljYXRpb25fYXBpIiwiY2hhdGJvdF9hcGkiLCJjb21wZXRlbmN5X2FwaSIsImNvbmZpZ3VyYXRpb25fYXBpIiwiZGVncmVlZF9hcGkiLCJmZWVkYmFja19hcGkiLCJnYWRnZXRfYXBpIiwibG9nZ2luZ19hcGkiLCJub3RpZmljYXRpb25fYXBpIiwicmVwb3J0X2FwaSIsInN1cnZleV9hcGkiLCJ6b29tX2FwaSJdLCJuYmYiOjE2ODk4MzY5NjcsImV4cCI6MTY4OTg1MTM2NywiaWF0IjoxNjg5ODM2OTY3LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjEwMDEwLyJ9.qadvBcp1f-KPYannWVnDQHuWYZkoe0o_Kaksvr0PNc-wASa7z7pfEAf84iIWnFtYbEeN3mfaaxwXLDSpwjaELywVQp3PpXBd6cgS___cmHfjGieD2IM4CizT30ITTOGifaU0krQDKJbaGXsY0B2nRsoDzx4s7taYOSzJ1Me-8CQ1lKyj-3CniuHMUfoh_P6LZns6SfS8Pb96MYmfUIQOHPxcesqUGKavPIgrg2J3qMjk8xB67DpfViXvzmLBmcKNYCCECoie4VRzbwJgjErLw8UOITQqv4DPuJX2plTDYKXyCnKz2e5q2UsrfbbUjbM7AhBP0PG7AqDXscmYiSMijQ'


# Replace 'your_secret_key' with the secret key or the public key used to sign the JWT
# Note: If your JWT is signed using a public/private key pair, provide the public key here.
# If it's a symmetrically signed token, use the same key that was used for signing.


# secret_key = 'SGZW7GQBPD1YMY6TZN4ZWPCKDQP05BX-OORJRZUN'


try:
    # Decoding the payload from the JWT
    decoded_payload = jwt.decode(access_token,algorithms='RS256',options={"verify_signature": False})
    username = decoded_payload.get('username')
    name = decoded_payload.get('name')
    decrypted_data = decrypt_aes_ecb([username,name])
    print(decrypted_data)
    # for key,value in decrypted_data.items():
    #     if key == name:
    #         print(value)
    #         # Extract the value associated with the old key
    #         value = decrypted_data.pop(key)

    #         decrypted_data[key] = value

    #         # Now the dictionary will have the updated key
    #         print(decrypted_data)
    #     elif key == username:
    #         print(value)
    # Extract 'username' and 'name' from the decoded payload
   
    # 'decoded_payload' will now contain the contents of the JWT's payload as a Python dictionary
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError as e:
    print("Invalid token or signature.",str(e))

# import jwt
# key='super-secret'
# payload={"id":"1","email":"myemail@gmail.com" }
# token = jwt.encode(payload, key)
# print (token)
# decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
# print (decoded)
# print (decoded["email"])

