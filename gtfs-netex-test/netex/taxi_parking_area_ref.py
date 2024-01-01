from dataclasses import dataclass
from .taxi_parking_area_ref_structure import TaxiParkingAreaRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiParkingAreaRef(TaxiParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
