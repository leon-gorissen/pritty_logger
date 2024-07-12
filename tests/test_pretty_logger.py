import unittest
from rich_logger.rich_logger import RichLogger

class TestRichLogger(unittest.TestCase):
    def test_log_info_message(self):
        logger = RichLogger("test")
        # Capture the output if necessary and assert expected results

if __name__ == "__main__":
    unittest.main()
