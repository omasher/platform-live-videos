BASE_URL = 'https://learning.oreilly.com'

COOKIES = {}

HEADERS = {}

RECORDINGS_QUERY = {
    'query': '\n  query UserLiveEvents(\n    $limit: Int!\n    $offset: Int!\n    $status: String\n    $tense: String!\n    $ordering: String!\n  ) {\n    userLiveEvents(\n      limit: $limit\n      offset: $offset\n      status: $status\n      tense: $tense\n      ordering: $ordering\n    ) {\n      count\n      results {\n        ...fields\n      }\n    }\n  }\n\n  \n  fragment fields on LiveEvent {\n    productIdentifier\n    seriesIdentifier\n    ourn\n    title\n    shortDescription\n    slug\n    startDatetime\n    endDatetime\n    cardTier\n    eventType\n    contentLevels\n    productType\n    marketingType {\n      id\n      name\n    }\n    registrationCloses\n    contributors {\n      fullName\n      headshotUrl2\n    }\n    sessions {\n      ourn\n      startTime\n      endTime\n    }\n    topics {\n      topicId\n      name\n      tagType\n    }\n    registrationInfo {\n      openSeats\n      userRegistrationStatus\n      cancelled\n      registrationIsOpen\n      waitlistStarted\n    }\n    upcomingLiveEventsInSeries\n  }\n\n',
    'variables': {
        'limit': 100,
        'offset': 0,
        'status': 'registered',
        'tense': 'past',
        'ordering': 'descending',
    },
    'operationName': 'UserLiveEvents',
}

LIVE_EVENTS_QUERY = {
    'query': '\n  query LiveEvents(\n    $limit: Int!\n    $offset: Int!\n    $topics: String\n    $publisher: String\n    $timeRanges: [[String]]\n    $onlyPrivate: Boolean!\n    $excludeClosed: Boolean!\n  ) {\n    liveEvents(\n      limit: $limit\n      offset: $offset\n      topics: $topics\n      publisher: $publisher\n      timeRanges: $timeRanges\n      onlyPrivate: $onlyPrivate\n      excludeClosed: $excludeClosed\n    ) {\n      count\n      results {\n        ...fields\n      }\n    }\n  }\n\n  \n  fragment fields on LiveEvent {\n    productIdentifier\n    seriesIdentifier\n    ourn\n    title\n    shortDescription\n    slug\n    startDatetime\n    endDatetime\n    cardTier\n    eventType\n    contentLevels\n    productType\n    marketingType {\n      id\n      name\n    }\n    registrationCloses\n    contributors {\n      fullName\n      headshotUrl2\n    }\n    sessions {\n      ourn\n      startTime\n      endTime\n    }\n    topics {\n      topicId\n      name\n      tagType\n    }\n    registrationInfo {\n      openSeats\n      userRegistrationStatus\n      cancelled\n      registrationIsOpen\n      waitlistStarted\n    }\n    upcomingLiveEventsInSeries\n  }\n\n',
    'variables': {
        'limit': 100,
        'offset': 0,
        'topics': None,
        'publisher': None,
        'timeRanges': None,
        'onlyPrivate': False,
        'excludeClosed': True,
    },
    'operationName': 'LiveEvents',
}

