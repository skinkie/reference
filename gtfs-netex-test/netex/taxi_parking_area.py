from dataclasses import dataclass, field
from netex.taxi_parking_area_version_structure import TaxiParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiParkingArea(TaxiParkingAreaVersionStructure):
    """A specific area where any taxi is able to safely park for a long period.

    +v1.2.2

    :ivar id: Identifier of TAXI PARKING AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
