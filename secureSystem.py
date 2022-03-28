import os
from os.path import exists

from cryptography.fernet import Fernet
KEY_FILE = "key.txt"


def openFileGui(fernet):
    encrypted = fernet.encrypt(original)
    with open('gui.py', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('gui.py', 'wb') as dec_file:
        dec_file.write(decrypted)

def openFileManualMonitor(fernet):
    encrypted = fernet.encrypt(original)
    with open('manualMonitor.py', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('manualMonitor.py', 'wb') as dec_file:
        dec_file.write(decrypted)
def openFileMonitor(fernet):
    encrypted = fernet.encrypt(original)
    with open('monitor.py', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('monitor.py', 'wb') as dec_file:
        dec_file.write(decrypted)

if __name__ == '__main__':
    key = Fernet.generate_key()
    fernet = Fernet(key)
    if exists(KEY_FILE):
        os.remove(KEY_FILE)
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    with open('gui.py', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('gui.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    with open('manualMonitor.py', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('manualMonitor.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    with open('monitor.py', 'rb') as file:
         original = file.read()
    encrypted = fernet.encrypt(original)
    with open('monitor.py', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    with open(KEY_FILE, 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    i = input("press 0 or 1")
    print(i)
    if i == "1":
        openFileGui(fernet)
        openFileManualMonitor(fernet)
        openFileMonitor(fernet)


