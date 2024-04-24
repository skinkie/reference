from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfLocatableSpotEnumeration(Enum):
    SEAT = "seat"
    BED = "bed"
    STANDING_SPACE = "standingSpace"
    WHEELCHAIR_SPACE = "wheelchairSpace"
    PUSHCHAIR_SPACE = "pushchairSpace"
    LUGGAGE_SPACE = "luggageSpace"
    BICYCLE_SPACE = "bicycleSpace"
    VEHICLE_SPACE = "vehicleSpace"
    SPECIAL_SPACE = "specialSpace"
