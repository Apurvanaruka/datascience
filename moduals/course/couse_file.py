import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__),"..")))


from payment import payment_file

def Couse():
    print("this is course function")

payment_file.Payment()