import concurrent.futures
import json 

import http.client

from .constants import (
    RECORDINGS_QUERY,
    LIVE_EVENTS_QUERY, get_header,
    BASE_URL)
from .logger import logger
from .utils import transform_data, EventType


def live_event(data_dict, data_path):
    results = data_dict['data'][data_path]['results']
    return results


def get_api_path(page=1, offset=None):
    return '/api/v1/attend/live-events/graphql'


def pull_data(event_type, pages, data_path=None):
    logger.info(f'Event type: {event_type}, Data Path: {data_path}')
    pull_live_data(event_type, pages, data_path)


def get_json_data(offset, event_type):
    query = RECORDINGS_QUERY if event_type == EventType.RECORDINGS \
        else LIVE_EVENTS_QUERY
    query['variables']['offset'] = offset
    return query


def load_url(page, event_type, url, data_path):
    offset = (page - 1) * 100
    json_data = get_json_data(offset=offset, event_type=event_type)
    headers = get_header(page=page)
    conn = http.client.HTTPSConnection(BASE_URL)
    conn.request(
        'POST',
        url,
        json.dumps(json_data),
        headers
    )
    response = conn.getresponse()
    response_data = response.read()
    data_dict = json.loads(response_data)
    conn.close()

    results = live_event(data_dict, data_path)
    logger.info(f'Page: {page}, Offset: {offset}')
    logger.info(f"Data loaded. Records = {len(results)}")

    return results


def pull_live_data(event_type, pages, data_path):
    result_list = []

    url = get_api_path() 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        fut = {executor.submit(load_url, page, event_type=event_type, url=url,
                               data_path=data_path): page for page in
               range(1, pages + 1)}
        for future in concurrent.futures.as_completed(fut):
            page = fut[future]
            try:
                data = future.result()
                result_list.extend(data)
            except concurrent.futures.CancelledError:
                logger.error(f"Error: {page} request was cancelled")
            except concurrent.futures.TimeoutError:
                logger.error(f"Error: {page} request timed out")

    transform_data(result_list, event_type=event_type)
