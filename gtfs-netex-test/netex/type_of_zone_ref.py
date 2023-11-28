from dataclasses import dataclass
from netex.type_of_zone_ref_structure import TypeOfZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfZoneRef(TypeOfZoneRefStructure):
    """
    Reference to a TYPE OF ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
