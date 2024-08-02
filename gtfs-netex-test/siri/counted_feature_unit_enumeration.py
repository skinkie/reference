from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CountedFeatureUnitEnumeration(Enum):
    BAYS = "bays"
    SEATS = "seats"
    OTHER_SPACES = "otherSpaces"
    DEVICES = "devices"
    VEHICLES = "vehicles"
    PERSONS = "persons"
    LITRES = "litres"
    SQUARE_METERS = "squareMeters"
    CUBIC_METERS = "cubicMeters"
    METERS = "meters"
    K_WH = "kWh"
    M_AH = "mAh"
    K_W = "kW"
    KG = "kg"
    A = "A"
    C = "C"
    OTHER = "other"
