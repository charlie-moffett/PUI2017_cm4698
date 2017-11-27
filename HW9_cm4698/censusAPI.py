import os

def getkey():
    with open(os.getenv("PUIDATA")+"/myAPI","r") as f:
        data = f.read()
    return data