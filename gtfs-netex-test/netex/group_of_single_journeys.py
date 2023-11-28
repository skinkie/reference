from dataclasses import dataclass, field
from netex.group_of_single_journeys_version_structure import GroupOfSingleJourneysVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfSingleJourneys(GroupOfSingleJourneysVersionStructure):
    """A GROUP OF SINGLE JOURNEYs, often known to its users by a name or a number.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
