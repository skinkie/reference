from dataclasses import dataclass, field
from netex.parking_tariff_version_structure import ParkingTariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingTariff(ParkingTariffVersionStructure):
    """
    A set of parking CHARGE BANDS that describe the cost if using a PARKING or
    PARKING AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
