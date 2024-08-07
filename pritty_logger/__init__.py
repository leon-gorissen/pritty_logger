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
from typing import Union, Dict, Any, List, Tuple, Optional
from rich.logging import RichHandler
from rich.pretty import pretty_repr


class RichLogger:
    def __init__(
        self,
        logger_name: str,
        level: int = logging.INFO,
        formatter: Optional[logging.Formatter] = None,
    ):
        """
        Initialize the RichLogger instance with a specific logger name.

        Args:
            logger_name (str): The name to be used for the logger.
        """
        self.logger = self.setup_logger(logger_name, level, formatter)
        self.level = level
        self.level_name = logging.getLevelName(self.level).lower()

    def setup_logger(
        self,
        logger_name: str,
        level: int = logging.INFO,
        formatter: Optional[logging.Formatter] = None,
    ) -> logging.Logger:
        """
        Set up the logger with a console handler and a file handler.

        Args:
            logger_name (str): The name to be used for the logger.
            level (int, optional): The logging level. Defaults to logging.INFO.
            formatter (logging.Formatter, optional): The formatter for the log messages.
                                                     Defaults to a standard formatter.

        Returns:
            logging.Logger: Configured logger instance.
        """
        if formatter is None:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

        logger = logging.getLogger(f"{logger_name}_logger")
        logger.setLevel(level)

        console_handler = RichHandler(rich_tracebacks=True)
        console_handler.setLevel(level)

        file_handler = logging.FileHandler(f"/var/log/{logger_name}.log")
        file_handler.setLevel(level)

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
            level (int, optional): Logger levels:  "debug", "info", "warning", "error", or "critical". Defaults to "info".
        """
        if isinstance(message, str):
            formatted_message = message
        else:
            formatted_message = pretty_repr(message)
        log_method = getattr(self.logger, level)
        log_method(formatted_message)

    def debug(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level DEBUG."""
        self.log(message, level="debug")

    def info(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level INFO."""
        self.log(message, level="info")

    def warn(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level WARNING."""
        self.log(message, level="warning")

    def warning(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level WARNING."""
        self.log(message, level="warning")

    def error(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level ERROR."""
        self.log(message, level="error")

    def critical(
        self, message: Union[str, Exception, Dict[Any, Any], List[Any], Tuple[Any, ...]]
    ):
        """Log a message with level CRITICAL."""
        self.log(message, level="critical")


# Example usage
if __name__ == "__main__":
    logger = RichLogger("example")
    logger.log("This is an info message")
    logger.log({"key": "value"}, level="debug")
