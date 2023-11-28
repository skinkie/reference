from dataclasses import dataclass, field
from netex.day_type_assignment_version_structure import DayTypeAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypeAssignment(DayTypeAssignmentVersionStructure):
    """Associates a DAY TYPE with an OPERATING DAY within a specific Calendar.

    A specification of a particular DAY TYPE which will be valid during
    a TIME BAND on an OPERATING DAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
