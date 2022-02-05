'''
YWRtaW4=   MTIz    30  1   January 2022
import os

total_size = 0
for dirpath, dirnames, filenames in os.walk('data'):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        # skip if it is symbolic link
        if not os.path.islink(fp):
            total_size += os.path.getsize(fp)

print(total_size)
'''
'''
from passlib.hash import pbkdf2_sha256

#Hashing entered username and password
username_entry_hash = pbkdf2_sha256.hash("admin", rounds = 200000, salt = b'29b721f5c4')
userpassword_entry_hash = pbkdf2_sha256.hash("123", rounds = 200000, salt = b'29b721f5c4')
print(username_entry_hash)
print(userpassword_entry_hash)
'''


#import sys

'''
i = "2021\n7\n18"
with open('data/bin/RecordDate.bin', 'wb+') as file:
    file.write((i).encode())
'''
import time

with open('C:/Users/babar/Desktop/SyserTech/SyserRetail/Basic/Source/data/bin/ClosingTime.bin', 'rb') as file:
    previous_date = file.read().decode()

print(previous_date.split('\n'))
time.sleep(100)

'''
from getmac import get_mac_address
ip_mac = get_mac_address(ip = "192.168.100.8")
print(ip_mac)
from scapy.layers.l2 import getmacbyip

mac = getmacbyip("192.168.100.1")

print(mac)
'''

'''
import sqlite3
db_conn = sqlite3.connect('data/databases/accounts.db')
db_cursor = db_conn.cursor()
db_cursor.execute('CREATE TABLE IF NOT EXISTS accounts(username BLOB, password BLOB, recordyear INT, recordmonth INT, recordday INT)')
db_conn.commit()
db_cursor.execute('INSERT INTO accounts VALUES(?, ?, ?, ?, ?)', (b'YWRtaW4=', b'MTIz', 2022, 1, 30))

import time
import sqlite3

#Accounts database connection
accounts_db_connection = sqlite3.connect('data/databases/accounts.db')
accounts_db_cursor = accounts_db_connection.cursor()

#Accounts database query username and password display
accounts_db_cursor.execute('SELECT username, password FROM accounts')
accounts_data_db = accounts_db_cursor.fetchall()
print(accounts_data_db)
accounts_data = []
for accounts_data_tuple in accounts_data_db:
    for username, password in enumerate(accounts_data_tuple):
        accounts_data.append(username)
        accounts_data.append(password)
print(accounts_data)

if 'YWRtaW4=' in accounts_data:
    print("YES")
else:
    print("NO")

#Accounts database connection closing
accounts_db_cursor.close()
accounts_db_connection.close()

time.sleep(100)
'''
'''
import time
import base64

var = 'NDU2'.encode("utf-8")
new_var = base64.b64decode(var).decode("utf-8")
print(new_var)
time.sleep(100)
'''
'''
import hashlib
m = hashlib.sha512()
m.update(b"Babar")
print(m.digest())

from passlib.hash import pbkdf2_sha256
hashed = pbkdf2_sha256.hash("123", rounds = 200000, salt = b'29b721f5c4')
print(hashed)
'''

#import uuid
#login_token = str(uuid.uuid4().hex[:12])
#print(f'LOGIN TOKEN: {login_token}')
