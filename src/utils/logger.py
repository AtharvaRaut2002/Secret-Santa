"""
Logger utility module for the Secret Santa assignment system.

This module sets up and returns a configured logger instance with both console and file handlers.
Logs are saved in the 'logs/' directory and are formatted with timestamps, module names, and log levels.

Usage:
    from src.utils.logger import setup_logger
    logger = setup_logger("ModuleName")
    logger.info("This is an info message.")
"""

import logging
import os

def setup_logger(name: str) -> logging.Logger:
    """Set up a logger with both file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Create file handler
    fh = logging.FileHandler("logs/secret_santa.log")
    fh.setLevel(logging.INFO)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers to logger if not already added
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
