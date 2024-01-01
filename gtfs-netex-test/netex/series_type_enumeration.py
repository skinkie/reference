from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeriesTypeEnumeration(Enum):
    STATION_TO_STATION = "stationToStation"
    ORIGIN_TO_BORDER = "originToBorder"
    BORDER_TO_DESTINATION = "borderToDestination"
    BORDER = "border"
    TRANSIT = "transit"
