import os
from pathlib import Path

import xlsxwriter

COLUMNS = ['EventID',
           'Date',
           'Authors',
           'Topic',
           'EventName',
           'EventDescription',
           ]


def get_static_path(event_type: str, output_path: str) -> str:
    home_dir = Path.home()
    return os.path.join(home_dir, output_path, event_type)


def write_to_excel(events, event_type: str, output_path: str):
    print(f'# of events found: {len(events)}')
    static_csv_path = get_static_path(f'{event_type}.xlsx', output_path)
    workbook = xlsxwriter.Workbook(static_csv_path)
    worksheet = workbook.add_worksheet()

    cols = COLUMNS
    if event_type == "events":
        cols.append('Registered')
    rows = []
    for event in events:
        event_id = event.get('event_id', None)
        if not event_id:
            continue
        topic = event.get('topic', None)
        description = event.get('description', None)
        name = event.get('name', '')
        authors = event.get('authors', None)
        url = event.get('url', None)
        event_id = f'=HYPERLINK("{url}", "{event_id}")'
        event_date = event.get('event_date', None)
        registered = True if event.get('registration_status'
                                       ) == 'registered' else False
        row = [event_id,
               event_date,
               authors,
               topic,
               name,
               description,
               ]
        if event_type == "events":
            row.append(registered)
        rows.append(row)

    for col_num, column_name in enumerate(cols):
        worksheet.write(0, col_num, column_name)

    for row_num, row_data in enumerate(rows):
        for col_num, cell_data in enumerate(row_data):
            worksheet.write(row_num + 1, col_num, cell_data)
    workbook.close()
