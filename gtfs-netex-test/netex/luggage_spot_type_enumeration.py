from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageSpotTypeEnumeration(Enum):
    RACK_ABOVE_SEATS = "rackAboveSeats"
    SPACE_UNDER_SEAT = "spaceUnderSeat"
    LUGGAGE_BAY = "luggageBay"
    LUGGAGE_COMPARTMENT = "luggageCompartment"
    LUGGAGE_VAN = "luggageVan"
    CYCLE_RACK = "cycleRack"
    OTHER = "other"
