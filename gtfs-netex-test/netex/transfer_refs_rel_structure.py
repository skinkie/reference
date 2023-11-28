from dataclasses import dataclass, field
from typing import List
from netex.access_ref import AccessRef
from netex.connection_ref import ConnectionRef
from netex.default_connection_ref import DefaultConnectionRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.site_connection_ref import SiteConnectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a TRANSFER.
    """
    class Meta:
        name = "transferRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
