from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_feature_ref import TypeOfFeatureRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FeatureTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "featureTypeRefs_RelStructure"

    type_of_feature_ref: list[TypeOfFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
