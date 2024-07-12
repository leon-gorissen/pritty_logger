#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: rich_logger

This module provides a RichLogger class for setting up and using a logger
with rich formatting. It uses the rich library to enhance the logging output
with color and formatting.

Classes:
    RichLogger: A class to set up and use a logger with rich formatting.

Usage example:
    logger = RichLogger("example")
    logger.log("This is an info message")
    logger.log({"key": "value"}, level="debug")
"""

import logging
from typing import Union, Dict, Any, List, Tuple
from rich.logging import RichHandler
from rich.pretty import pretty_repr


class RichLogger:
    def __init__(self, logger_name: str):
        """
        Initialize the RichLogger instance with a specific logger name.

        Args:
            logger_name (str): The name to be used for the logger.
        """
        self.logger = self.setup_logger(logger_name)

    def setup_logger(self, logger_name: str) -> logging.Logger:
        """
        Set up the logger with a console handler and a file handler.

        Args:
            logger_name (str): The name to be used for the logger.

        Returns:
            logging.Logger: Configured logger instance.
        """
        logger = logging.getLogger(f"{logger_name}_logger")
        logger.setLevel(logging.INFO)

        console_handler = RichHandler(rich_tracebacks=True)
        console_handler.setLevel(logging.INFO)

        file_handler = logging.FileHandler(f"/var/log/dynamics_learning/{logger_name}.log")
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

    def log(
        self,
        message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]],
        level: str = "info",
    ):
        """
        Log messages using rich formatting.

        Args:
            message (Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]): Log message.
            level (str, optional): Logger levels: "debug", "info", "warning", "error", "critical". Defaults to "info".
        """
        if isinstance(message, str):
            formatted_message = message
        else:
            formatted_message = pretty_repr(message)

        log_method = getattr(self.logger, level)
        log_method(formatted_message)


# Example usage
if __name__ == "__main__":
    logger = RichLogger("example")
    logger.log("This is an info message")
    logger.log({"key": "value"}, level="debug")
