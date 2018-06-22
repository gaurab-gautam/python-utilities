# imports
from time import strftime, localtime
import logging
import os.path


# log names
TIMEOUT_LOG = 'timeout_log'
ERROR_LOG = 'error_log'

# filepath to log files
TIMEOUT_LOG_FILE_PATH = 'path/to/timeout/log/file' 	# example: '~/logs/timeout_log.txt'
ERROR_LOG_FILE_PATH = 'path/to/error/log/file' 		# example: '~/logs/error_log.txt'

# logger initialize
def init():
    # setup loggers
    __setup_logger(TIMEOUT_LOG, TIMEOUT_LOG_FILE_PATH)
    __setup_logger(ERROR_LOG, ERROR_LOG_FILE_PATH)

    
# logger settings   
def __setup_logger(logger_name, log_file, level=logging.DEBUG):
    log_setup = logging.getLogger(logger_name)
    formatter = logging.Formatter('\n%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    log_setup.setLevel(level)
    log_setup.addHandler(fileHandler)
    

#  log to file
def __log(msg, level, logname):
    if logname == ERROR_LOG: 
        log = logging.getLogger(ERROR_LOG)
    elif logname == TIMEOUT_LOG: 
        log = logging.getLogger(TIMEOUT_LOG) 
    
    # log info for message
    if level == logging.INFO: 
        log.info(msg) 
    # log exception for error
    elif level == logging.ERROR: 
        log.exception(msg)
    

def log_timeout(message):
    __log(message, logging.INFO, TIMEOUT_LOG)


def log_error(message):
    __log(message, logging.ERROR, ERROR_LOG)


