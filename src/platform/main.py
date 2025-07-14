import sys

from .api import pull_data
from .logger import logger
from .utils import EventType, output_var

def is_valid_event_type(e_type):
    return e_type in EventType.__members__.values()


if __name__ == "__main__":
    usage = "Usage: python script.py <events|recordings> <pages> <output_path>"
    if len(sys.argv) != 4:
        logger.error(usage)
        sys.exit(1)


    try:
        event_type = sys.argv[1]
        if not is_valid_event_type(event_type):
            raise ValueError("Invalid event type")
        pages = int(sys.argv[2])
        output_path = sys.argv[3]
        output_var.set(output_path)
    except ValueError as e:
        logger.error(usage)
        sys.exit(1)

    data_path = None
    if event_type == EventType.EVENTS:
        data_path = "liveEvents"
    elif event_type == EventType.RECORDINGS:
        data_path = "userLiveEvents"
    pull_data(event_type, pages=pages, data_path=data_path)
