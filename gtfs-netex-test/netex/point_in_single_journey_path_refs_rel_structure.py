from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.point_in_single_journey_path_ref import PointInSingleJourneyPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointInSingleJourneyPathRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of POINT IN SINGLE JOURNEY PATHs.
    """
    class Meta:
        name = "PointInSingleJourneyPathRefs_RelStructure"

    point_in_single_journey_path_ref: PointInSingleJourneyPathRef = field(
        metadata={
            "name": "PointInSingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
