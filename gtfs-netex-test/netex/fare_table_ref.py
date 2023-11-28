from dataclasses import dataclass
from netex.fare_table_ref_structure import FareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRef(FareTableRefStructure):
    """
    Reference to a FARE TABLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
