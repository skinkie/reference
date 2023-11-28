from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.service_access_code_ref import ServiceAccessCodeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessCodeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of SERVICE ACCESS CODEs.
    """
    class Meta:
        name = "serviceAccessCodeRefs_RelStructure"

    service_access_code_ref: ServiceAccessCodeRef = field(
        metadata={
            "name": "ServiceAccessCodeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
