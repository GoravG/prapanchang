import logging
import os


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.INFO)  # Default to INFO

            if os.environ.get("DEBUG"):
                cls._instance.logger.setLevel(logging.DEBUG)

            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
        return cls._instance.logger


def get_logger():
    return Logger()


logger = get_logger()
