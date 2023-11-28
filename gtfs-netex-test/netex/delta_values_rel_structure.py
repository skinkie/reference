from dataclasses import dataclass, field
from typing import List
from netex.delta_value import DeltaValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeltaValuesRelStructure:
    """
    A collection of one or more DELTA VALUEs.
    """
    class Meta:
        name = "deltaValues_RelStructure"

    delta_value: List[DeltaValue] = field(
        default_factory=list,
        metadata={
            "name": "DeltaValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
