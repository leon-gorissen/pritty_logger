import logging
from pritty_logger import RichLogger


def test_info_log(caplog):
    logger = RichLogger("test", logging.INFO)
    with caplog.at_level(logging.INFO):
        logger.info("This is an info message")
        logger.debug("This is a debug message. It shouldn't be logged.")

    assert "This is an info message" in caplog.text
    assert "This is a debug message" not in caplog.text
    caplog.clear()


def test_debug_log(caplog):
    logger = RichLogger("test", logging.DEBUG)
    with caplog.at_level(logging.DEBUG):
        logger.debug("This is a debug message")

    assert "This is a debug message" in caplog.text
    caplog.clear()


def test_warning_log(caplog):
    logger = RichLogger("test", logging.WARNING)
    with caplog.at_level(logging.WARNING):
        logger.warning("This is a warning message")
        logger.debug("This is a debug message. It shouldn't be logged.")

    assert "This is a warning message" in caplog.text
    assert "This is a debug message" not in caplog.text
    caplog.clear()


def test_error_log(caplog):
    logger = RichLogger("test", logging.ERROR)
    with caplog.at_level(logging.ERROR):
        logger.error("This is an error message")
        logger.log("This is a debug message. It shouldn't be logged.", "debug")

    assert "This is an error message" in caplog.text
    assert "This is a debug message" not in caplog.text
    caplog.clear()


def test_critical_log(caplog):
    logger = RichLogger("test", logging.CRITICAL)
    with caplog.at_level(logging.CRITICAL):
        logger.critical("This is a critical message")
        logger.log("This is a debug message. It shouldn't be logged.", "debug")

    assert "This is a critical message" in caplog.text
    assert "This is a debug message" not in caplog.text
    caplog.clear()
