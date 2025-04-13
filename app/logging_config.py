import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logging():
    log_format = '%(asctime)s %(levelname)s %(name)s %(message)s'
    formatter = jsonlogger.JsonFormatter(log_format)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)

setup_logging()