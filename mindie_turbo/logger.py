import logging
import sys
from pathlib import Path

_LOG_FILE = Path(__file__).resolve().parent / "app.log"


def get_logger(package_name: str) -> logging.Logger:
    logger = logging.getLogger(package_name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(name)s - %(filename)s:%(lineno)d - %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(_LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
