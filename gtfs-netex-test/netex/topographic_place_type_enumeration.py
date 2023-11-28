from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TopographicPlaceTypeEnumeration(Enum):
    """
    Allowed values for classifying TOPOGRAPHIC PLACEs.

    :cvar CONTINENT:
    :cvar INTERREGION:
    :cvar COUNTRY:
    :cvar PRINCIPALITY:
    :cvar STATE:
    :cvar PROVINCE: Country, province, principality - e.g. E.g. England,
        Wales.
    :cvar REGION:
    :cvar COUNTY:
    :cvar AREA:
    :cvar CONURBATION:
    :cvar CITY: Locality is a city.
    :cvar MUNICIPALITY:
    :cvar QUARTER:
    :cvar SUBURB: Locality is an urban sub-area.
    :cvar TOWN: Locality is a town.
    :cvar URBAN_CENTRE: Locality is a City Centre or Town Centre ZONE of
        another town or city locality.
    :cvar DISTRICT:
    :cvar PARISH:
    :cvar VILLAGE: Locality is a village.
    :cvar HAMLET: Locality is a hamlet.
    :cvar PLACE_OF_INTEREST: Locality is a place of interest whose name
        is distinct from another locality.
    :cvar OTHER: Locality is none of the other types.
    :cvar UNRECORDED: Locality type is not yet specified.
    """
    CONTINENT = "continent"
    INTERREGION = "interregion"
    COUNTRY = "country"
    PRINCIPALITY = "principality"
    STATE = "state"
    PROVINCE = "province"
    REGION = "region"
    COUNTY = "county"
    AREA = "area"
    CONURBATION = "conurbation"
    CITY = "city"
    MUNICIPALITY = "municipality"
    QUARTER = "quarter"
    SUBURB = "suburb"
    TOWN = "town"
    URBAN_CENTRE = "urbanCentre"
    DISTRICT = "district"
    PARISH = "parish"
    VILLAGE = "village"
    HAMLET = "hamlet"
    PLACE_OF_INTEREST = "placeOfInterest"
    OTHER = "other"
    UNRECORDED = "unrecorded"
