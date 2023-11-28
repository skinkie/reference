from dataclasses import dataclass
from netex.transport_administrative_zone_ref_structure import TransportAdministrativeZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportAdministrativeZoneRef(TransportAdministrativeZoneRefStructure):
    """
    Reference to a TRANSPORT ADMINISTRATIVE ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
