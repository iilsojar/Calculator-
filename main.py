import user_interface
import calc_function
from logg import logging

logging.info("Start programm")

def button_click():
    value_a = user_interface.get_value()
    value_b = user_interface.get_value()
    calc_function.init(value_a, value_b)
    result = user_interface.choice()
    user_interface.user_inter(result)


