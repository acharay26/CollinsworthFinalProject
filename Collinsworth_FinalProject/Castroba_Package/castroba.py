'''
Created on Dec 5, 2023

@author: Benjamin
'''
from cryptography.fernet import Fernet

import json


def movie():

    # Your key for decryption

    key = b't7WyuS-VCj3eb9HE0OHPhva2b30FSid88Z5nSiYUo0c='


    with open('movie_quote.json', 'r') as json_file: # reads json file

        data = json.load(json_file)

       

    cipher_suite = Fernet(key)

   

    encrypted_collinsworth = data.get("Collinsworth", [])

    decrypted_collinsworth = []


    for item in encrypted_collinsworth:

        decrypted_item = cipher_suite.decrypt(item.encode()).decode()

        decrypted_collinsworth.append(decrypted_item)

   

    # Print the decrypted data

    print(decrypted_collinsworth)

