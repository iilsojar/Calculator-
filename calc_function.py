from logg import logging

logging.info("in process...")

x = int(0) 
y = int(0) 

def init (a, b):
    global x
    global y
    x = a
    y = b

def sum(a, b): 
    return  a + b 
    
def mult(a, b): 
    return a * b
 
def div(a, b): 
    return a / b

def sub(a, b): 
    return a - b


