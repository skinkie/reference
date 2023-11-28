from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.single_journey_path_ref import SingleJourneyPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyPathRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SINGLE JOURNEY PATHs.
    """
    class Meta:
        name = "singleJourneyPathRefs_RelStructure"

    single_journey_path_ref: SingleJourneyPathRef = field(
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
