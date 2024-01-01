from dataclasses import dataclass, field
from typing import List
from .trace import Trace


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TracesRelStructure:
    class Meta:
        name = "traces_RelStructure"

    trace: List[Trace] = field(
        default_factory=list,
        metadata={
            "name": "Trace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
