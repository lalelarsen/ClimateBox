from settings import getSettings
from importScript import test

settings = getSettings()
print("start")
print(settings["Temperature"])

settings["Temperature"] = 10

test()
settings["Temperature"] = 20
test()
settings["Temperature"] = settings["Temperature"] + 20

test()