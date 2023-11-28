from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_service_feature_ref import TypeOfServiceFeatureRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfServiceFeatureRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a TYPEs of SERVICE FEATURE.
    """
    class Meta:
        name = "typeOfServiceFeatureRefs_RelStructure"

    type_of_service_feature_ref: List[TypeOfServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
