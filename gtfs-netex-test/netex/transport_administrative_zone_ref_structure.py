from dataclasses import dataclass
from netex.administrative_zone_ref_structure import AdministrativeZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportAdministrativeZoneRefStructure(AdministrativeZoneRefStructure):
    """
    Type for a reference to a TRANSPORT ADMINISTRATIVE ZONE.
    """
