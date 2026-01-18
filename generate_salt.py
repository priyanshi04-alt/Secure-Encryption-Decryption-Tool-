import os

salt = os.urandom(16)

with open("salt.key", "wb") as f:
    f.write(salt)

print("Salt generated")
