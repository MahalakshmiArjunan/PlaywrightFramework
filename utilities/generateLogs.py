import logging

# logging.basicConfig(filename="../logs/logfile1.log", format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%m/%d/%y %I:%M:%S %p',level=logging.INFO)
#
# log = logging.getLogger()
# log.error(("I'm in error block"))
# log.info("This is Mahalakshmi Arjunan")

def log():
    logging.basicConfig(filename="../logs/logfile1.log", format='%(asctime)s: %(levelname)s: %(message)s',
                         datefmt='%m/%d/%y %I:%M:%S %p',level=logging.INFO)
    logger = logging.getLogger()
    return logger

logger = log()
logger.info("This is from a function or utility")