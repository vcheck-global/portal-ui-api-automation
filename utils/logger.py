# utils/logger.py
import logging
import os

def setup_logger(log_file="logs/automation.log"):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Remove any existing handlers (important!)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode='w'),
            logging.StreamHandler()  # Optional: also print logs to console
        ]
    )
