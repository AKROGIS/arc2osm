# Based on the Places Data Schema revision 6 (5/18/2015)
# https://github.com/nationalparkservice/places-data/wiki/Places-Data-Schema-Guide
# with ogr2osm, the GIS field names are case sensitive
# with arc2osm, all GIS field names are converted to upper case
# all osm/Places tags should be lower case

# All config files must have defaults, fieldmap, altnames and valuemap

# default tags for road *lines* in Places
defaults = {
    'highway': 'road',
    'oneway': 'no',
    'access': 'no'
}

# values map one to one from field name to OSM tag
fieldmap = {
    # GIS_FieldName : Places Tag
    'RDNAME': 'name',
    'RDALTNAMES': 'nps:road_alt_names',
    'RDLABEL': 'nps:road_label',
    'RDSTATUS': 'nps:road_status',
    'RDCLASS': 'nps:road_class',
    'RDMAINTAINER': 'nps:road_maintainer',
    'LANES': 'lanes',
    'ROUTEID': 'nps:route_id',
    'RTENUMBER': 'nps:route_number'
}

# alternate GIS field names.
altnames = {
    # GIS Standard FieldName: List of alternate spellings of field name
    'RDNAME': ['NAME', 'ROADNAME', 'RD_NAME', 'ROAD_NAME'],
    'RDALTNAMES': ['ALTNAMES', 'ROADALTNAMES', 'RD_ALTNAMES',
                   'ROAD_ALTNAMES'],
    'RDLABEL': ['LABEL', 'ROADLABEL', 'RD_LABEL', 'ROAD_LABEL'],
    'RDSTATUS': ['STATUS', 'ROADSTATUS', 'RD_STATUS', 'ROAD_STATUS'],
    'RDCLASS': ['CLASS', 'ROADCLASS', 'RD_CLASS', 'ROAD_CLASS'],
    'RDMAINTAINER': ['MAINTAINER', 'ROADMAINTAINER', 'RD_MAINTAINER',
                     'ROAD_MAINTAINER'],
    'ROUTEID': ['ROUTE', 'ROUTE_ID'],
    'RTENUMBER': ['RTE_NUMBER', 'ROUTENUMBER', 'ROUTE_NUMBER']
}

# GIS field names where different values map to a specific set of Places tags
valuemap = {
    # GIS_FieldName : {GIS_Value: {tag:value, ... }, ...}
    'RDCLASS': {
        'Primary': {'highway': 'primary'},
        'Secondary': {'highway': 'secondary'},
        'Local': {'highway': 'residential'},
        '4WD': {
            'highway': 'road',
            '4wd_only': 'yes'
        },
        'Service':  {
            'highway': 'service',
            'access': 'private'
        },
        'Private': {'highway': 'road'}
    },
    'RDSTATUS': {
        'Existing': {'access': 'yes'},
        'Decommissioned': {'access': 'no'},
        'Temporarily Closed': {'access': 'no'},
        'Proposed': {
            'access': 'no',
            'highway': 'proposed'  # conflict with RDCLASS
        },
        'Planned':  {
            'access': 'no',
            'highway': 'proposed'  # conflict with RDCLASS
        }
    },
    'RDSURFACE': {
        'Asphalt': {'surface': 'asphalt'},
        'Concrete': {'surface': 'concrete'},
        'Brick/Pavers': {'surface': 'paving_stones'},
        'Cobblestone': {'surface': 'cobblestone'},
        'Gravel': {'surface': 'gravel'},
        'Sand': {'surface': 'sand'},
        'Native or Dirt': {'surface': 'ground'},
        'Unpaved Other': {'surface': 'unpaved'},
        'Paved Other': {'surface': 'paved'}
    },
    'ONEWAY': {
        'With Digitized': {'oneway': 'yes'},
        'Against Digitized': {'oneway': '-1'}
    }
}
