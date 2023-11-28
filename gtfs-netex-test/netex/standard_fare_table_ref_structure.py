from dataclasses import dataclass
from netex.fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StandardFareTableRefStructure(FareTableRefStructure):
    """
    Type for Reference to a FARE STANDARD FARE TABLE.
    """
