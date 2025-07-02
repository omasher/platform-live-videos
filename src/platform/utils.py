import logging
from enum import Enum
from typing import List

from .constants import BASE_URL
from .events import write_to_excel

MAX_SHORT_TEXT_LENGTH =  32
MAX_LONG_TEXT_LENGTH = 66 

class EventType(str, Enum):
    RECORDINGS = 'recordings'
    EVENTS = 'events'

class ColTextType(str, Enum):
    SHORT = 'short'
    LONG = 'long'

def truncate_text(text: str, col_text_type: ColTextType):
    truncated_text = text
    if col_text_type == ColTextType.SHORT and len(text) > MAX_SHORT_TEXT_LENGTH:
        truncated_text = f'{text[:MAX_SHORT_TEXT_LENGTH]}...'
    if col_text_type == ColTextType.LONG and len(text) > MAX_LONG_TEXT_LENGTH:
        truncated_text = f'{text[:MAX_SHORT_TEXT_LENGTH]}...'        
    return truncated_text

def transform_data(data: List[dict], event_type):
    results = []
    transformed_data = {}
    for item in data:
        event_id = item.get("productIdentifier", "")
        topic = " ".join([topic.get("name", "") for topic in item
                         .get("topics", [])])
        name = item.get("title", "")
        name = truncate_text(name, col_text_type=ColTextType.LONG)
        description = (item.get("shortDescription", "")
                       .replace("\n", ""))
        event_date = item.get("startDatetime", "").split("T")[0]
        authors =  " ".join(
            [contributor.get("fullName", "") for contributor in item
            .get("contributors", [])])
        authors = truncate_text(authors, col_text_type=ColTextType.SHORT)
        slug = item.get("slug", "")
        series_identifier = item.get("seriesIdentifier", "")
        url = f"{BASE_URL}/live-events/{slug}/{series_identifier}/{event_id}"
        registration_status = (item.get("registrationInfo")
                               .get("userRegistrationStatus"))

        transformed_data = {
            "event_id": event_id,
            "topic": topic,
            "name": name,
            "description": description,
            "event_date": event_date,
            "authors": authors,
            "url": url,
            "registration_status": registration_status
        }
        results.append(transformed_data)

    write_to_excel(results, event_type=event_type)
