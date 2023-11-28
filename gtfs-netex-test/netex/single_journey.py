from dataclasses import dataclass, field
from netex.single_journey_version_structure import SingleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourney(SingleJourneyVersionStructure):
    """The planned movement of a public transport vehicle on a DAY TYPE from the
    start point to the end point of a JOURNEY PATTERN on a specified ROUTE.

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
