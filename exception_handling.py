
try:
    print(x)
except NameError:
    print("variable x is not defined")    
else:
    print("Everything went wrong")
    

x = -1

if x < 0:
    raise Exception("sorry, no numbers below zero")        