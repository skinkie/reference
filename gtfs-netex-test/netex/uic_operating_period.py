from dataclasses import dataclass, field
from netex.uic_operating_period_version_structure import UicOperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicOperatingPeriod(UicOperatingPeriodVersionStructure):
    """
    An OPERATING PERIOD coded in UIC style as a bit string between two dates.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
