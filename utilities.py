import logging as L
import time

file = 'Logs/log.txt'


# Function for logs capturing
def log(level, message, file):
    L.basicConfig(level=L.INFO,
                  filename=file,
                  filemode="a",
                  format="%(asctime)-12s%(levelname)s%(message)s",
                  datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO": L.info(message)
    if level == "WARNING": L.warning(message)
    if level == "ERROR": L.error(message)
    if level == "CRITICAL": L.critical(message)




# Function for Screenshot capturing
def screenshot(drv):
    """Take screenshot with current date and  time"""
    folder = "Logs/screenshot/"
    time_string = time.asctime().replace(":", " ")
    file_name = folder + time_string + ".png"
    drv.save_screenshot(file_name)
