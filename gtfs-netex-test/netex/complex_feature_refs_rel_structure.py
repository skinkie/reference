from dataclasses import dataclass, field
from netex.complex_feature_ref import ComplexFeatureRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeatureRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to COMPLEX FEATUREs.
    """
    class Meta:
        name = "complexFeatureRefs_RelStructure"

    complex_feature_ref: ComplexFeatureRef = field(
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
