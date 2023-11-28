from dataclasses import dataclass
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Zone(ZoneVersionStructure):
    """
    A two-dimensional PLACE within the service area of a public transport operator
    (administrative zone, TARIFF ZONE, ACCESS ZONE, etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
