from dataclasses import dataclass
from netex.access_zone_ref_structure import AccessZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessZoneRef(AccessZoneRefStructure):
    """
    Reference to a SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
