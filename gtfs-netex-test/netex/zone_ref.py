from dataclasses import dataclass
from netex.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneRef(ZoneRefStructure):
    """
    Reference to a ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
