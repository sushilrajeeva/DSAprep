import random
import string

keys = ["id", "username", "password"]
users = ["sushilrajeev", "sachiverma", "sunilrajeev", "spongbob101"]

def gen_password() ->  str:
    return "".join(random.choices(string.printable, k = 9))

data = [{key: index if key == "id" else value if key == "username" else gen_password() for key in keys} for index, value in enumerate(users)]

print(data)


from sys import *
from collections import *
from math import *

def rotateArray(arr: list, n: int) -> []:
    # Write your code from here.
    first_ele = arr[0]
    arr = [arr[index] for index in range(1,n)]
    arr.append(first_ele)
    print(arr)
    return arr

print(rotateArray([1, 2, 3, 4, 5], 5))