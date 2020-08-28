import cred
from cryptography.fernet import Fernet
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()
f = Fernet(key)
email = f.decrypt(cred.email.encode())
password = f.decrypt(cred.password.encode())
print(email.decode(),password.decode())