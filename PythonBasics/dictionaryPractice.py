import random
import string

keys = ["id", "username", "password"]
users = ["sushilrajeev", "sachiverma", "sunilrajeev", "spongbob101"]

def gen_password() ->  str:
    return "".join(random.choices(string.printable, k = 9))

data = [{key: index if key == "id" else value if key == "username" else gen_password() for key in keys} for index, value in enumerate(users)]

print(data)