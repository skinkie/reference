from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .online_service_ref import OnlineServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceOperatorRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "onlineServiceOperatorRefs_RelStructure"

    online_service_ref: List[OnlineServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "OnlineServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
