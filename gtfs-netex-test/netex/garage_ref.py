from dataclasses import dataclass
from netex.garage_ref_structure import GarageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GarageRef(GarageRefStructure):
    """
    Reference to a GARAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
