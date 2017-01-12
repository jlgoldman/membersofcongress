import csv_unicode

REP_HEADER_ROW = (
    'bioguide_id', 'first_name', 'last_name', 'state_code', 'state_name',
    'district_number', 'district_code', 'district_ordinal', 'party', 'chamber',
    'title', 'title_short', 'website',
    )

OFFICE_HEADER_ROW = (
    'handle', 'bioguide_id', 'type', 'name', 'line1', 'line2',
    'city', 'state_code', 'zip', 'phone', 'latitude', 'longitude',
    )

def json_to_rep_csv(js, rep_output_filename):
    rep_outfile = open(rep_output_filename, 'w')
    rep_writer = csv_unicode.UnicodeWriter(rep_outfile)
    rep_writer.writerow(REP_HEADER_ROW)
    for rep in js:
        row = [rep.get(attr) for attr in REP_HEADER_ROW]
        rep_writer.writerow(row)
    rep_outfile.close()

def json_to_office_csv(js, office_output_filename):
    office_outfile = open(office_output_filename, 'w')
    office_writer = csv_unicode.UnicodeWriter(office_outfile)
    office_writer.writerow(OFFICE_HEADER_ROW)
    for rep in js:
        for office in rep['offices']:
            office_row = [office.get(attr) for attr in OFFICE_HEADER_ROW if attr != 'bioguide_id']
            office_row.insert(OFFICE_HEADER_ROW.index('bioguide_id'), rep['bioguide_id'])
            office_writer.writerow(office_row)
    office_outfile.close()

if __name__ == '__main__':
    import json
    import sys
    js = json.load(open(sys.argv[1]))
    json_to_rep_csv(js, 'members.csv')
    json_to_office_csv(js, 'offices.csv')