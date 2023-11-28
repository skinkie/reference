from dataclasses import dataclass
from netex.standard_fare_table_ref_structure import StandardFareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StandardFareTableRef(StandardFareTableRefStructure):
    """
    Reference to a STANDARD FARE TABLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
