from dataclasses import dataclass, field

from .trace import Trace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TracesRelStructure:
    class Meta:
        name = "traces_RelStructure"

    trace: list[Trace] = field(
        default_factory=list,
        metadata={
            "name": "Trace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
