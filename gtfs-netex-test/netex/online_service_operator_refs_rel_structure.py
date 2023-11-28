from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.online_service_ref import OnlineServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceOperatorRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of ONLINE SERVICEs.
    """
    class Meta:
        name = "onlineServiceOperatorRefs_RelStructure"

    online_service_ref: List[OnlineServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "OnlineServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
