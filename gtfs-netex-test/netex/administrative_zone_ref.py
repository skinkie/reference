from dataclasses import dataclass
from netex.administrative_zone_ref_structure import AdministrativeZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdministrativeZoneRef(AdministrativeZoneRefStructure):
    """
    Reference to an ADMINISTRATIVE ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
