from app import logging

def add(a,b):
    logging.debug("Addition is taking place")
    return a+b

def sub(a,b):
    logging.debug("Substraction is taking place")
    return a+b

def mul(a,b):
    logging.debug("Multiplication is taking place")
    return a+b

def div(a,b):
    logging.debug("Division is taking place")
    return a+b

logging.info("Addition started")
add(5,3)
logging.info("Multiplocation started")
mul(5,3)
logging.info("Substraction started")
sub(5,3)
logging.info("Division started")
div(15,3)

