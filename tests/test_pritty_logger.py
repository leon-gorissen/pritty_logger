import logging
from pritty_logger import RichLogger


def test_log(caplog):
    messages = {
        "debug": "This is a debug message",
        "info": "This is an info message",
        "warning": "This is a warning message",
        "error": "This is an error message",
        "critical": "This is a critical message",
    }

    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    for level_name, logging_level in levels.items():
        log_instance = RichLogger("test", logging_level)
        with caplog.at_level(logging_level):
            # Log all messages
            for log_level, message in messages.items():
                log_instance.log(message, level=log_level)

            # Check that messages at or above the current level are in the log
            for log_level, message in messages.items():
                if levels[log_level] >= logging_level:
                    assert message in caplog.text
                else:
                    assert message not in caplog.text

            caplog.clear()  # Clear caplog for the next iteration


def test_info_log(caplog):
    logger = RichLogger("test")
    with caplog.at_level(logging.INFO):
        logger.info("This is an info message")

    assert "This is an info message" in caplog.text
    caplog.clear()


def test_debug_log(caplog):
    logger = RichLogger("test", logging.DEBUG)
    with caplog.at_level(logging.DEBUG):
        logger.debug("This is a debug message")

    assert "This is a debug message" in caplog.text
    caplog.clear()


def test_warning_log(caplog):
    logger = RichLogger("test")
    with caplog.at_level(logging.WARNING):
        logger.warning("This is a warning message")

    assert "This is a warning message" in caplog.text
    caplog.clear()


def test_error_log(caplog):
    logger = RichLogger("test")
    with caplog.at_level(logging.ERROR):
        logger.error("This is an error message")

    assert "This is an error message" in caplog.text
    caplog.clear()


def test_critical_log(caplog):
    logger = RichLogger("test")
    with caplog.at_level(logging.CRITICAL):
        logger.critical("This is a critical message")

    assert "This is a critical message" in caplog.text
    caplog.clear()
