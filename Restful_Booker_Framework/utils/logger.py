import os
import logging
from datetime import datetime


def setup_logger():
    """
    Sets up the logger for the application.
    Configures logging with the format:
         <timestamp> - <log level> - <message>
    The log file is stored in 'logs/ directory'.
    Returns:
        logging.Logger: The configured logger instance.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists('logs'):
        os.mkdir('logs')
    logging.basicConfig(filename=f"logs/test_log_{timestamp}.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s"
                        )
    return logging.getLogger(__name__)


logger = setup_logger()
