from dataclasses import dataclass, field

from .delta_value import DeltaValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeltaValuesRelStructure:
    class Meta:
        name = "deltaValues_RelStructure"

    delta_value: list[DeltaValue] = field(
        default_factory=list,
        metadata={
            "name": "DeltaValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
