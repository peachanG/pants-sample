import time
import logging
import absl.logging
from typing import Any


def set_logging_basic_config(log_level: str = "INFO") -> None:
    """Build logging logger
    Args:
        log_level (str): log_level.
                         Defaults to "INFO".
    """
    # NOTE: https://github.com/tensorflow/tensorflow/issues/27045
    logging.root.removeHandler(absl.logging._absl_handler)
    absl.logging._warn_preinit_stderr = False

    log_fmt = logging.Formatter('%(asctime)s %(name)s %(lineno)d '
                                '[%(levelname)s][%(funcName)s] %(message)s')
    s_handler = logging.StreamHandler()
    s_handler.setLevel(log_level)
    s_handler.setFormatter(log_fmt)
    logger = logging.getLogger()
    # clean out any default added handlers from import errors etc
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(s_handler)
    logger.setLevel(log_level)
