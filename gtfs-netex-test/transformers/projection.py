from decimal import Decimal, ROUND_HALF_UP
from itertools import chain

from pyproj import Transformer
from pyproj.exceptions import CRSError

from netex import Polygon, PosList, Pos, LocationStructure2

transformers = {}

def get_transformer_by_srs_name(location, crs_to) -> Transformer:
    if hasattr(location, 'pos') and location.pos is not None:
        srs_name = location.pos.srs_name or location.srs_name or 'urn:ogc:def:crs:EPSG::4326'
    else:
        srs_name = location.srs_name or 'urn:ogc:def:crs:EPSG::4326'

    if srs_name == crs_to:
        return None

    mapping = f"{srs_name}_{crs_to}"
    transformer = transformers.setdefault(mapping, None)
    if transformer is None:
        try:
            transformer = Transformer.from_crs(srs_name, crs_to) # TODO: Test if we can use accuracy instead of quantitize later
        except CRSError:
            # TODO: Implement logging rule that handles error
            raise
            pass
        except:
            raise
        transformers[mapping] = transformer
    return transformer

def project_location_4326(location, quantize='0.000001'):
    crs_to = 'urn:ogc:def:crs:EPSG::4326'
    if location.pos is not None:
        transformer = get_transformer_by_srs_name(location, crs_to)
        if transformer is not None:
            latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
        else:
            latitude = location.pos.value[0]
            longitude = location.pos.value[1]

        location.longitude = Decimal(longitude).quantize(Decimal(quantize), ROUND_HALF_UP)
        location.latitude = Decimal(latitude).quantize(Decimal(quantize), ROUND_HALF_UP)
        location.srs_name = crs_to
        location.pos = None

    elif location.srs_name not in (None, 'EPSG:4326', 'urn:ogc:def:crs:EPSG::4326'):
        print("TODO: Crazy not WGS84")

def project_location(location: LocationStructure2, crs_to: str, quantize='0.000001'):
    if location.pos is not None:
        transformer = get_transformer_by_srs_name(location, crs_to)
        if transformer is not None:
            x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
            x = Decimal(x).quantize(Decimal(quantize), ROUND_HALF_UP)
            y = Decimal(y).quantize(Decimal(quantize), ROUND_HALF_UP)
            location.srs_name = crs_to
            location.pos = Pos(value=[x, y], srs_name=crs_to, srs_dimension=2)

    elif location.longitude is not None and location.latitude is not None:
        transformer = get_transformer_by_srs_name(location, crs_to)
        if transformer is not None:
            x, y = transformer.transform(location.latitude, location.longitude)
            x = Decimal(x).quantize(Decimal(quantize), ROUND_HALF_UP)
            y = Decimal(y).quantize(Decimal(quantize), ROUND_HALF_UP)
            location.srs_name = crs_to
            location.pos = Pos(value=[x, y], srs_name=crs_to, srs_dimension=2)

    else:
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
        linestring.pos_or_point_property_or_pos_list = [PosList(value=[Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in chain(*zip(pxx, pyy))], srs_dimension=srs_dimension)]
    elif srs_dimension == 3:
        pxx, pyy, pzz = transformer.transform(xx, yy, zz)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=[Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in chain(*zip(pxx, pyy, pzz))], srs_dimension=srs_dimension)]

    # TODO: I would really want to apply the crs_to here

def project_polygon(polygon: Polygon, crs_to):
    mapping = f"{polygon.srs_name}_{crs_to}"
    transformer = transformers.get(mapping, Transformer.from_crs(polygon.srs_name, crs_to))
    transformers[mapping] = transformer
    project_linestring2(transformer, polygon.exterior.linear_ring)
    for interior in polygon.interior:
        project_linestring2(transformer, interior)
    if crs_to == 'EPSG:4326':
        polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value = [Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value]
        for interior in polygon.interior:
            interior.linear_ring.pos_or_point_property_or_pos_list[0].value = [
                Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in
                interior.linear_ring.pos_or_point_property_or_pos_list[0].value]
    polygon.srs_name = crs_to
