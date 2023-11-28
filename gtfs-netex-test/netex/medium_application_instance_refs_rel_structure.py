from dataclasses import dataclass, field
from netex.medium_application_instance_ref import MediumApplicationInstanceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumApplicationInstanceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of MEDIUM APPLICATION INSTANCEs.
    """
    class Meta:
        name = "mediumApplicationInstanceRefs_RelStructure"

    medium_application_instance_ref: MediumApplicationInstanceRef = field(
        metadata={
            "name": "MediumApplicationInstanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
