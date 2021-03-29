#!/usr/bin/env python
# coding: utf-8

# # QTM 385
# 
# ***
# 
# ## Midterm
# 
# Student: [2302860]

# In[15]:


import sys
import os.path
from os import path

def count_lines(f):
    line_count = 0
    for i in f:
        line_count += 1
    return line_count

    
def readfirst_last_5(lines):
    for i in range(5):
        sys.stdout.write(lines[i])
    
    print("...")
    
    for i in range(-5,0):
        sys.stdout.write(lines[i])

def show_text():
    if path.exists("message.txt"):
        f = open("message.txt", "r") 
        line_count = count_lines(f)
        f = open("message.txt", "r") 
        lines = f.readlines()
        
        if line_count >10:
            readfirst_last_5(lines)
        
        else:
            for i in range(line_count):
                sys.stdout.write(lines[i])
    else:
        print("Error. 'message.txt' is not available.")
    
def encrypt(c):
    rd.seed(key)
    mixed_alpha = low_alpha[:]
    rd.shuffle(mixed_alpha)
    mapping = str.maketrans(string.ascii_lowercase, "".join(mixed_alpha))
    return c.translate(mapping)

def readfirst_last_5_encrypt(lines):
    
    for i in range(5):
        sys.stdout.write(encrypt(lines[i]))
                         
    print("...")
                         
    for i in range(-5,0):
        sys.stdout.write(encrypt(lines[i]))

def show_encrypt():
    if path.exists("encrypted.txt"):
        f = open("encrypted.txt", "r") 
        line_count = count_lines(f)
        f = open("encrypted.txt", "r") 
        lines = f.readlines()
        if line_count >10:
            readfirst_last_5(lines)
        else:
            for i in range(line_count):
                sys.stdout.write(lines[i])
    else:
        print("Error. 'encrypted.txt' is not available.")
    
def set_key():
    key = ''
    while not key:
        try:
            key = int(input(''))
            if key not in range(100,1000):
                raise ValueError
            else:
                return key
        except ValueError:
            key = ''
            print("Error: it should be a number between 100 and 999")
    
def show_map():
    import sys
    
    rd.seed(key)
    mixed_alpha = low_alpha[:]
    rd.shuffle(mixed_alpha)
    
    sys.stdout.write("The encryption map is: \n")
    for i in range(26):
        sys.stdout.write(string.ascii_lowercase[i] + " => " + "".join(mixed_alpha)[i] + "\t")
        
    sys.stdout.write("\n\nAnd the decryption map is:\n")
    for i in range(26):
        sys.stdout.write("".join(mixed_alpha)[i] + " => " + string.ascii_lowercase[i] + "\t")

                         
def save_encrypt():
    if path.exists("message.txt"):
        g = open("encrypted.txt", "w")
        f = open("message.txt", "r")
        g.write(encrypt(f.read()))
        g.close()
    else:
        print("Error. 'message.txt' is not available.")

def decrypt(d):
    rd.seed(key)
    mixed_alpha = low_alpha[:]
    rd.shuffle(mixed_alpha)
    mapping = str.maketrans("".join(mixed_alpha), string.ascii_lowercase)
    return d.translate(mapping)

def readfirst_last_5_decrypt(d):
    lines = d.readlines()
    for i in range(5):
        sys.stdout.write(decrypt(lines[i]))
                         
    print("...")
                         
    for i in range(-5,0):
        sys.stdout.write(decrypt(lines[i]))

def show_decrypt():
    try:
        d = open("encrypted.txt","r")
        line_count = count_lines(d)
        d = open("encrypted.txt","r")
        
        if line_count > 10:
            readfirst_last_5_decrypt(d)
        else:
            print(decrypt(d.read()))
    except FileNotFoundError:
        print("error. The decryption failed")


# In[16]:


# Set an initial value for choice other than the value for 'quit'.
import random as rd
import string

key = set_key()
        
low_alpha = []
for i in range(26):
    low_alpha.append(string.ascii_lowercase[i])

function_name = ''

# We get line_count as variable instead of calling message.txt to count everytime because if 
# message.txt file gets larger it will take more time to load the data multiple times.

# Start a loop that runs until the user enters the value for 'quit'.
while function_name != 'bye':
    
    # Ask for the user's choice.
    function_name = input("\nEnter your command here: ")
    
    # Respond to the user's choice.
    if function_name == 'show-text':
        show_text()
    elif function_name == 'show-encrypt':
        show_encrypt()
    elif function_name == 'show-key':
        print("The encryption key is: " + str(key))
    elif function_name == 'set-key':
        key = set_key()
    elif function_name == 'show-map':
        show_map()
    elif function_name == 'encrypt':
        save_encrypt()
    elif function_name == 'decrypt':
        show_decrypt()
    elif function_name == 'bye':
        print('Bye have a nice day')
    else:
        print("\nPlease Enter a Proper Function Name\n")


# In[ ]:




