from dataclasses import dataclass, field

from .delta import Delta

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeltasRelStructure:
    class Meta:
        name = "deltas_RelStructure"

    delta: list[Delta] = field(
        default_factory=list,
        metadata={
            "name": "Delta",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
