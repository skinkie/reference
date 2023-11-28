from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.open_transport_mode_ref import OpenTransportModeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OpenTransportModeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TRANSPORT MODE.
    """
    class Meta:
        name = "openTransportModeRefs_RelStructure"

    open_transport_mode_ref: List[OpenTransportModeRef] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
