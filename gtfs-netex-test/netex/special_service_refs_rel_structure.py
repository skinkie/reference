from dataclasses import dataclass, field
from typing import Optional, Union

from .dated_special_service_ref import DatedSpecialServiceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "specialServiceRefs_RelStructure"

    special_service_ref: Optional[Union[DatedSpecialServiceRef, SpecialServiceRef]] = field(
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
        },
    )
