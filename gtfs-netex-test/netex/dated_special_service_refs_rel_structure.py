from dataclasses import dataclass, field
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedSpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list references to a DATED SPECIAL SERVICE.
    """
    class Meta:
        name = "DatedSpecialServiceRefs_RelStructure"

    dated_special_service_ref: DatedSpecialServiceRef = field(
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
