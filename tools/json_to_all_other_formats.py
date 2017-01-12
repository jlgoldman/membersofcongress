'''
Takes the master JSON file, specified by name as a command-line argument,
and converts it to all other output formats. Run this from the root directory:
python tools/json_to_all_other_formats.py members.json
'''

import codecs
import copy
import json

import json_to_csv
import json_to_geojson
import json_to_postgis
import json_to_sql

def main(members_json_fname):
    js = json.load(open(members_json_fname))

    geojson_str = json_to_geojson.json_to_geojson(copy.deepcopy(js))
    geojson_file = codecs.open('offices.geojson', 'w', 'utf-8')
    geojson_file.write(geojson_str)
    geojson_file.close()

    sql_str = json_to_sql.json_to_sql(copy.deepcopy(js))
    sql_file = codecs.open('members.sql', 'w', 'utf-8')
    sql_file.write(sql_str)
    sql_file.close()

    postgis_str = json_to_postgis.json_to_postgis(copy.deepcopy(js))
    postgis_file = codecs.open('members.postgis.sql', 'w', 'utf-8')
    postgis_file.write(postgis_str)
    postgis_file.close()

    json_to_csv.json_to_rep_csv(js, 'members.csv')
    json_to_csv.json_to_office_csv(js, 'offices.csv')

    print 'Done. Wrote offices.geojson, members.sql, members.postgis.sql, members.csv, and offices.csv'

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print 'Usage: python %s /path/to/members.json' % sys.argv[0]
        sys.exit(0)
    main(sys.argv[1])
