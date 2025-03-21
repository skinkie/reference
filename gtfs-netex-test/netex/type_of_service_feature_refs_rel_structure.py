from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_service_feature_ref import TypeOfServiceFeatureRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfServiceFeatureRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfServiceFeatureRefs_RelStructure"

    type_of_service_feature_ref: list[TypeOfServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
