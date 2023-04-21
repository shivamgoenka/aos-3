import hashlib
import re
import random
import string

i = 0

while True:  # try up to 1,000,000 strings
    s = str(random.randint(0,1000000000000))
    if( i % 10000000 == 0):
        print(s)
        print(i)
    hashh = hashlib.md5(s.encode()).digest().decode("latin-1")

    if "'or'" in hashh:
        print(f"loose match: {s}")
        print(f"Hash: {hashh}")
    i = i+1
