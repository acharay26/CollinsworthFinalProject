#Name: Aditya Achar, Ben Castro, Cameron Vegh, Riley McCullough
#email: mccullrw@mail.uc.edu, acharay@mail.uc.edu, castroba@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that decrypt a JSON file in multiple ways
#Citations: next to code that citation used
#Anything else that's relevant: Happy holidays

import json

def decrypt_collinsworth(json_file_path, txt_file_path):
    with open(json_file_path, 'r') as json_file: # reads json file
        encrypted_indices_dict = json.load(json_file)

    with open(txt_file_path, 'r') as txt_file: # reads txt file
        lines = txt_file.readlines()

    if 'Collinsworth' in encrypted_indices_dict:
        collinsworth_indices = encrypted_indices_dict['Collinsworth']
        words = []  # List to store words

        for index in collinsworth_indices: # for loop to append each word into list
            index = index.rstrip(' ')# removes unecessary whitespaces
            line_number = int(index)#converts indexed numbers to integers
            words.append(lines[line_number].strip())  # Append each word to the list

        decrypted_message = " ".join(words)  # Join the words into a single string - source(https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python)

    return decrypted_message

def location_print():   
    #stores key, json file, and txt file into variables used in functions
    json_file_path = 'EncryptedGroupHintsFall2023Section001.json'
    txt_file_path = 'english_2.txt'

    #stores fucntion into object
    hidden_message = decrypt_collinsworth(json_file_path, txt_file_path)
    print(hidden_message)