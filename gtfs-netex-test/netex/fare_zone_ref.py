from dataclasses import dataclass
from netex.fare_zone_ref_structure import FareZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareZoneRef(FareZoneRefStructure):
    """
    Reference to a FARE ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
