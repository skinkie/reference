from dataclasses import dataclass
from netex.zone_projection_ref_structure import ZoneProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneProjectionRef(ZoneProjectionRefStructure):
    """
    Reference to a PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
