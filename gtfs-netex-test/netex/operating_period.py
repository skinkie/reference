from dataclasses import dataclass, field
from netex.operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingPeriod(OperatingPeriodVersionStructure):
    """
    A continuous interval of time between two OPERATING DAYs which will be used to
    define validities.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
