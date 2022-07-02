import uuid
import logging
 
def check_valid_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)