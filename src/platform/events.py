import os

import xlsxwriter

COLUMNS = ['EventID',
           'Topic',
           'EventName',
           'EventDescription',
           'Date',
           'Authors']


def get_static_path(event_type: str):
    script_directory = os.path.dirname(os.path.abspath(__name__))
    return os.path.join(script_directory, "static", event_type)


def write_to_excel(events, event_type):
    print(f'# of events found: {len(events)}')
    static_csv_path = get_static_path(f'{event_type}.xlsx')
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
               topic,
               name,
               description,
               event_date,
               authors]
        if event_type == "events":
            row.append(registered)
        rows.append(row)

    for col_num, column_name in enumerate(cols):
        worksheet.write(0, col_num, column_name)

    for row_num, row_data in enumerate(rows):
        for col_num, cell_data in enumerate(row_data):
            worksheet.write(row_num + 1, col_num, cell_data)
    workbook.close()
