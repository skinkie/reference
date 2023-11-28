from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.point_of_interest_classification_ref import PointOfInterestClassificationRef
from netex.point_of_interest_classification_view import PointOfInterestClassificationView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationsViewsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of POINT OF INTEREST SPACEs.
    """
    class Meta:
        name = "pointOfInterestClassificationsViews_RelStructure"

    point_of_interest_classification_ref_or_point_of_interest_classification_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestClassificationRef",
                    "type": PointOfInterestClassificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationView",
                    "type": PointOfInterestClassificationView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
