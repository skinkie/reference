from dataclasses import dataclass
from netex.garage_point_ref_structure import GaragePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GaragePointRef(GaragePointRefStructure):
    """
    Reference to a GARAGE POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
