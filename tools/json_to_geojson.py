import copy
import json

def json_to_geojson(js):
    features = []
    for rep in js:
        offices = rep['offices']
        del rep['offices']
        for office in offices:
            if not office['latitude']:
                continue
            geometry = {
                'type': 'Point',
                'coordinates': [office['longitude'], office['latitude']],
                }
            del office['latitude']
            del office['longitude']
            feature = {
                'type': 'Feature',
                'geometry': geometry,
                'properties': office,
            }
            feature['properties']['rep'] = copy.deepcopy(rep)
            features.append(feature)
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features,
    }
    return json.dumps(feature_collection, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    import sys
    print json_to_geojson(json.load(open(sys.argv[1])))