from dataclasses import dataclass
from netex.fare_table_column_ref_structure import FareTableColumnRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableColumnRef(FareTableColumnRefStructure):
    """
    Reference to a FARE TABLE COLUMN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
