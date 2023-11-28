from dataclasses import dataclass, field
from netex.time_demand_type_version_structure import TimeDemandTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandType(TimeDemandTypeVersionStructure):
    """An indicator of traffic conditions or other factors which may affect vehicle
    run or wait times.

    It may be entered directly by the scheduler or defined by the use of
    TIME BANDs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
