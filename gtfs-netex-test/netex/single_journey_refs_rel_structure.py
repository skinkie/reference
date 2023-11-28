from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.single_journey_ref import SingleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SINGLE JOURNEYs.
    """
    class Meta:
        name = "singleJourneyRefs_RelStructure"

    single_journey_ref: SingleJourneyRef = field(
        metadata={
            "name": "SingleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
