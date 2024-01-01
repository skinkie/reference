from dataclasses import dataclass
from .fare_table_column_ref_structure import FareTableColumnRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableColumnRef(FareTableColumnRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
