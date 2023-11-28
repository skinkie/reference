from dataclasses import dataclass, field
from netex.tariff_zone_version_structure import TariffZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffZone(TariffZoneVersionStructure):
    """
    A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix
    system.

    :ivar id: Reference to a TYPE OF  TARIFF ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
