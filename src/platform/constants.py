BASE_URL = "https://example.com"


def get_header(page):
    return {
    'User-Agent': '',
    'Accept': 'application/graphql-response+json, application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': f'https://example.com/path/?page={page}',
    'content-type': 'application/json',
    'Origin': 'https://example.com',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
}


RECORDINGS_QUERY = {
    "operationName": "UserLiveEvents",
    "query": "\n  query UserLiveEvents(\n    $limit: Int!\n    $offset: Int!\n    $status: String\n    $tense: String!\n    $ordering: String!\n  ) {\n    userLiveEvents(\n      limit: $limit\n      offset: $offset\n      status: $status\n      tense: $tense\n      ordering: $ordering\n    ) {\n      count\n      results {\n        ...fields\n      }\n    }\n  }\n\n  \n  fragment fields on LiveEvent {\n    productIdentifier\n    seriesIdentifier\n    ourn\n    title\n    shortDescription\n    slug\n    startDatetime\n    endDatetime\n    cardTier\n    eventType\n    contentLevels\n    productType\n    marketingType {\n      id\n      name\n    }\n    academies {\n      slug\n    }\n    registrationCloses\n    contributors {\n      fullName\n      headshotUrl2\n    }\n    sessions {\n      ourn\n      startTime\n      endTime\n    }\n    topics {\n      topicId\n      name\n      tagType\n    }\n    registrationInfo {\n      openSeats\n      userRegistrationStatus\n      cancelled\n      registrationIsOpen\n      waitlistStarted\n    }\n    upcomingLiveEventsInSeries\n  }\n\n",
    "variables": {
        "limit": 100,
        "offset": 0,
        "ordering": "descending",
        "status": "registered",
        "tense": "past",
    },
}

LIVE_EVENTS_QUERY = {
    "operationName": "LiveEvents",
    "query": "\n  query LiveEvents(\n    $limit: Int!\n    $offset: Int!\n    $topics: String\n    $publisher: String\n    $timeRanges: [[String]]\n    $onlyPrivate: Boolean!\n    $excludeClosed: Boolean!\n  ) {\n    liveEvents(\n      limit: $limit\n      offset: $offset\n      topics: $topics\n      publisher: $publisher\n      timeRanges: $timeRanges\n      onlyPrivate: $onlyPrivate\n      excludeClosed: $excludeClosed\n    ) {\n      count\n      results {\n        ...fields\n      }\n    }\n  }\n\n  \n  fragment fields on LiveEvent {\n    productIdentifier\n    seriesIdentifier\n    ourn\n    title\n    shortDescription\n    slug\n    startDatetime\n    endDatetime\n    cardTier\n    eventType\n    contentLevels\n    productType\n    marketingType {\n      id\n      name\n    }\n    academies {\n      slug\n    }\n    registrationCloses\n    contributors {\n      fullName\n      headshotUrl2\n    }\n    sessions {\n      ourn\n      startTime\n      endTime\n    }\n    topics {\n      topicId\n      name\n      tagType\n    }\n    registrationInfo {\n      openSeats\n      userRegistrationStatus\n      cancelled\n      registrationIsOpen\n      waitlistStarted\n    }\n    upcomingLiveEventsInSeries\n  }\n\n",
    "variables": {
        "excludeClosed": True,
        "limit": 100,
        "offset": 0,
        "onlyPrivate": False,
        "publisher": None,
        "timeRanges": None,
        "topics": None,
    },
}
