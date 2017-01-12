import copy
import json
import sqlite3

CREATE_REP_SQL = '''
CREATE TABLE rep (
    bioguide_id varchar(7),
    first_name varchar(50),
    last_name varchar(50),
    state_code varchar(2),
    state_name varchar(50),
    district_number integer,
    district_code varchar(4),
    district_ordinal varchar(8),
    party varchar(20),
    chamber varchar(10),
    title varchar(20),
    title_short varchar(4),
    website varchar(255)
);
'''

CREATE_OFFICE_SQL = '''
CREATE TABLE office (
    handle varchar(60),
    bioguide_id varchar(7),
    type varchar(8),
    name varchar(50),
    line1 varchar(255),
    line2 varchar(255),
    city varchar(100),
    state_code varchar(2),
    zip varchar(10),
    phone varchar(14),
    latitude real,
    longitude real
);
'''

REP_INSERT_SQL = '''
INSERT INTO rep VALUES (
    :bioguide_id,
    :first_name,
    :last_name,
    :state_code,
    :state_name,
    :district_number,
    :district_code,
    :district_ordinal,
    :party,
    :chamber,
    :title,
    :title_short,
    :website
);
'''

OFFICE_INSERT_SQL = '''
INSERT INTO office VALUES (
    :handle,
    :bioguide_id,
    :type,
    :name,
    :line1,
    :line2,
    :city,
    :state_code,
    :zip,
    :phone,
    :latitude,
    :longitude
);
'''

def json_to_sql(js):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(CREATE_REP_SQL)
    cursor.execute(CREATE_OFFICE_SQL)
    for rep in js:
        cursor.execute(REP_INSERT_SQL, rep)
        for office in rep['offices']:
            office_params = copy.deepcopy(office)
            office_params['bioguide_id'] = rep['bioguide_id']
            cursor.execute(OFFICE_INSERT_SQL, office_params)
    conn.commit()
    return '\n'.join(conn.iterdump())

if __name__ == '__main__':
    import sys
    print json_to_sql(json.load(open(sys.argv[1])))
