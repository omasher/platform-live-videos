import logging
from enum import Enum
from typing import List

from .constants import BASE_URL
from .events import write_to_excel


class EventType(str, Enum):
    RECORDINGS = 'recordings'
    EVENTS = 'events'


def transform_data(data: List[dict], event_type):
    results = []
    transformed_data = {}
    for item in data:
        event_id = item.get("productIdentifier", "")
        topic = " ".join([topic.get("name", "") for topic in item
                         .get("topics", [])])
        name = item.get("title", "")
        description = (item.get("shortDescription", "")
                       .replace("\n", ""))
        event_date = item.get("startDatetime", "").split("T")[0]
        authors = " ".join(
            [contributor.get("fullName", "") for contributor in item
            .get("contributors", [])])
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
