# Members of Congress in Various Formats

This project is a repository of members of Congress and their contact information.
Most notably, in contains address, phone numbers, and latlngs for *district offices*.

This project was created specifically because no database of district office
information seemed to exist, since while Washington DC office information
is available through official Senate and House XML feeds, district office
info is strewn about as unstructured data on Congressional websites.

## Usage

Data are intended to be ready-to-use as much as possible. A variety of formats
containing the same data are provided for convenience.

### JSON

The master file is `members.json`, containing basic information about each
member of Congress and attached to each member is a list of their offices,
including both Washington DC and district offices.

### CSV

For spreadsheet use, the same data have been split into `members.csv` and
`offices.csv`. The `bioguide_id` field, the seemingly official id assigned
by Congressional clerk websites, can be used as a join key between
member and office

### SQL

For populating a SQL database, `members.sql` contains ready-to-execute
SQL commands for creating a schema and filling rows for both members
and their offices, once again using `bioguide_id` as the join key.
The SQL syntax is basic and should be compatible with sqlite, PostgreSQL, and MySQL.

#### sqlite

```
# Create and populate the DB
cat members.sql | sqlite3 members.sqlite
# Connect to the DB
sqlite3 members.sqlite
```

#### PostgreSQL

```
# Create the DB
createdb members
psql -d members -f members.sql
# Connect to the DB
psql members
```

#### PostGIS

Since office locations have been pre-geocoded into latitudes and longitudes,
an additional SQL file is provided to those who wish to use PostGIS with
PostgreSQL so that geospatial queries can be done on office locations.
For that, do the same as above with a regular SQL database but make sure
PostGIS is [installed](http://postgis.net/install/) first, and then
use `members.postgis.sql` instead.

```
# Create the DB
createdb members
psql -d members -f members.postgis.sql
# Connect to the DB
psql members
```

### GeoJSON

Since there are coordinates for each office, an alternate JSON file containing
GeoJSON has been provided, that is ready to be imported in any compatible GIS
program or [Google Maps](https://developers.google.com/maps/documentation/javascript/datalayer#load_geojson)
or perhaps client-side geospatial libraries like [Turf](http://turfjs.org/)

## The Data

The data were initally collected from individual Congressional websites the week of January 9, 2017. Washington DC offices are included for all 541 members. At least
one district office is included for 527 members; 14 newly-elected members have yet
to publish district office information on their still-being-constructed websites.

This repository will be updated as soon as information for the remaining offices
is available.

### How Was It Collected?

A clipping tool was built, capable of parsing most standard, multi-line address
blocks, that possibly contained an office name and phone number. Office addresses
were then copy-pasted from Congressional websites into the tool. In the ~10% of
cases where the parser did not work, addresses were manually cleaned/adjusted
until they could be parsed. Addresses were then sanity-checked and geocoded.

### Contributing

If data seems to be incorrect or incomplete, please help contribute!
The master file is *`members.json`*, please make changes to that file
and submit a pull request. You can optionally convert from the master JSON
file to all other formats in a single command:

```
python tools/json_to_all_other_formats.py members.json
```

I am currently working on a public-facing version of the clipping tool
to make contributing easier and to help with updates after future elections.