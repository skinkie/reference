from dataclasses import dataclass
from netex.fare_table_row_ref_structure import FareTableRowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRowRef(FareTableRowRefStructure):
    """
    Reference to a FARE TABLE ROW.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
