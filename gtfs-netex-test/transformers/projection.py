from decimal import Decimal, ROUND_HALF_UP
from itertools import chain

from pyproj import Transformer

from netex import Polygon, PosList, Pos

transformers = {}

def get_transformer_by_srs_name(location, crs_to, generator_defaults: dict) -> Transformer:
    if location.pos is not None:
        srs_name = location.srs_name or location.pos.srs_name or generator_defaults.get('DefaultLocationsystem', 'urn:ogc:def:crs:EPSG::4326')
    else:
        srs_name = location.srs_name or generator_defaults.get('DefaultLocationsystem', 'urn:ogc:def:crs:EPSG::4326')

    if srs_name == crs_to:
        return None

    mapping = f"{srs_name}_{crs_to}"
    transformer = transformers.setdefault(mapping, None)
    if transformer is None:
        transformer = Transformer.from_crs(srs_name, crs_to)
        transformers[mapping] = transformer
    return transformer

def project_location_4326(location, generator_defaults: dict):
    if location.pos is not None:
        transformer = get_transformer_by_srs_name(location, 'urn:ogc:def:crs:EPSG::4326')
        if transformer is not None:
            latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
        else:
            latitude = location.pos.value[0]
            longitude = location.pos.value[1]

        location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.pos = None

    elif location.srs_name not in (None, 'EPSG:4326', 'urn:ogc:def:crs:EPSG::4326') and generator_defaults['DefaultLocationsystem'] not in ('EPSG:4326', 'urn:ogc:def:crs:EPSG::4326'):
        print("TODO: Crazy not WGS84")

def project_linestring2(transformer, linestring):
    srs_dimension = linestring.srs_dimension if hasattr(linestring, 'srs_dimension') and linestring.srs_dimension else 2
    xx = []
    yy = []
    zz = []
    if isinstance(linestring.pos_or_point_property_or_pos_list[0], PosList):
        xx = linestring.pos_or_point_property_or_pos_list[0].value[0::srs_dimension]
        yy = linestring.pos_or_point_property_or_pos_list[0].value[1::srs_dimension]
        if srs_dimension >= 2:
            zz = linestring.pos_or_point_property_or_pos_list[0].value[2::srs_dimension]
    elif isinstance(linestring.pos_or_point_property_or_pos_list[0], Pos):
        xx = [pos.value[0] for pos in linestring.pos_or_point_property_or_pos_list]
        yy = [pos.value[1] for pos in linestring.pos_or_point_property_or_pos_list]
        if srs_dimension >= 2:
            zz = [pos.value[2] for pos in linestring.pos_or_point_property_or_pos_list]

    if srs_dimension == 2:
        pxx, pyy = transformer.transform(xx, yy)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy))))]
    elif srs_dimension == 3:
        pxx, pyy, pzz = transformer.transform(xx, yy, zz)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy, pzz))))]

def project_polygon(polygon: Polygon, generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    project_linestring2(transformer, polygon.exterior.linear_ring)
    for interior in polygon.interior:
        project_linestring2(transformer, interior)
    if crs_to == 'EPSG:4326':
        polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value = [Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value]
        for interior in polygon.interior:
            interior.linear_ring.pos_or_point_property_or_pos_list[0].value = [
                Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in
                interior.linear_ring.pos_or_point_property_or_pos_list[0].value]
