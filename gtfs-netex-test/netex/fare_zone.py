from dataclasses import dataclass, field
from netex.fare_zone_version_structure import FareZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareZone(FareZoneVersionStructure):
    """
    A specialization of TARIFF ZONE to include FARE SECTIONs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
