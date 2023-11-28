from dataclasses import dataclass, field
from netex.default_interchange_version_structure import DefaultInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultInterchange(DefaultInterchangeVersionStructure):
    """A quality parameter fixing the acceptable duration (standard and maximum)
    for an INTERCHANGE to be planned between two SCHEDULED STOP POINTs.

    This parameter will be used to control whether any two VEHICLE
    JOURNEYs serving those points may be in connection.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
