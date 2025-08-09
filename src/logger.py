import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path for the logs folder
logs_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_folder, exist_ok=True)  # Create only the folder

# Full log file path
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")

