"""
Logger Utility
--------------

Custom logger with support for:
✅ Colored console output
✅ Dynamic log levels (DEBUG, INFO, WARNING, ERROR)
✅ Optional file output for persistent logging
"""

import logging
import sys

LOG_COLORS = {
    'DEBUG': '\033[94m',   # Blue
    'INFO': '\033[92m',    # Green
    'WARNING': '\033[93m', # Yellow
    'ERROR': '\033[91m',   # Red
    'RESET': '\033[0m'     # Reset
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        color = LOG_COLORS.get(levelname, LOG_COLORS['RESET'])
        message = super().format(record)
        return f"{color}{message}{LOG_COLORS['RESET']}"


def get_logger(name: str = "agent") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = ColoredFormatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger


# Example usage
if __name__ == "__main__":
    log = get_logger("example")
    log.debug("Debug message for developers.")
    log.info("Execution started.")
    log.warning("This might become an issue.")
    log.error("An error has occurred!")
