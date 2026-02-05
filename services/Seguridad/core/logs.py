import logging
from logging.handlers import TimedRotatingFileHandler
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | "
        "%(filename)s:%(lineno)d | %(funcName)s | %(message)s"
    )

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    debug_handler = logging.StreamHandler()
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    error_handler = TimedRotatingFileHandler(
        "logs/errors.log",
        when="midnight",
        backupCount=7
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)
