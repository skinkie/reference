from dataclasses import dataclass
from netex.fare_unit_ref_structure import FareUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitRefStructure(FareUnitRefStructure):
    """
    Type for Reference to a GEOGRAPHICAL UNIT.
    """
