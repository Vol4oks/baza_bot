import os

from dotenv import load_dotenv

load_dotenv()

admins = os.getenv("admins").split(',')
users = os.getenv("users").split(',')

print(type(admins), admins)
print(type(users), users)