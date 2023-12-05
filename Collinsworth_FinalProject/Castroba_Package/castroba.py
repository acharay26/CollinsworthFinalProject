#Name: Aditya Achar, Ben Castro, Cameron Vegh, Riley McCullough
#email: mccullrw@mail.uc.edu, acharay@mail.uc.edu, castroba@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that decrypt a JSON file in multiple ways
#Citations: next to code that citation used
#Anything else that's relevant: Happy holidays
from cryptography.fernet import Fernet
import json

def movie():
    # key
    key = b't7WyuS-VCj3eb9HE0OHPhva2b30FSid88Z5nSiYUo0c='

    with open('movie_quote.json', 'r') as json_file: # reads json file

        data = json.load(json_file)

       

    cipher_suite = Fernet(key)# decrypts key

   

    encrypted_collinsworth = data.get("Collinsworth", [])# pulls collinsworth string

    decrypted_collinsworth = []# creates empty list for decrypted string



    for item in encrypted_collinsworth:# loop for decrypted string

        decrypted = cipher_suite.decrypt(item.encode()).decode()

        decrypted_collinsworth.append(decrypted)

   

    # Print the movie name

    print(decrypted_collinsworth)