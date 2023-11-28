from dataclasses import dataclass, field
from typing import Optional
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list references to a SPECIAL SERVICE.
    """
    class Meta:
        name = "specialServiceRefs_RelStructure"

    dated_special_service_ref_or_special_service_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
