"""

Basic Structure of a logger - 
    1. __root__ logger - Fully configured including all handlers, formatters and filters.
    2. module level logger - Only used to pass the message to the __root__ logger via propogation. 
"""
import logging 
import json
import logging.config
logger = logging.getLogger(name="my_app")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple" : {
            "format": "%(levelname)s: %(message)s",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout"]
        }
    },
}

def setup_logger():
    # with open('./config.json') as f:
    #     logging_config = json.load(f)
    #     logging.config.dictConfig(config=logging_config)
    logging.config.dictConfig(config=logging_config)

def main():
    setup_logger()
    logger.info("first log message")
    logger.critical("First Critical Message")
    print(f"Printing somthings to stdout")

if __name__ == "__main__":
    main()