from dataclasses import dataclass, field
from netex.relief_opportunity_version_structure import ReliefOpportunityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefOpportunity(ReliefOpportunityVersionStructure):
    """A time in a BLOCK where a vehicle passes a RELIEF POINT.

    This opportunity may or may not be actually used for a relief.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
