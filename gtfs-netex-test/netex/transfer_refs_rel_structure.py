from dataclasses import dataclass, field
from typing import Union

from .access_ref import AccessRef
from .connection_ref import ConnectionRef
from .default_connection_ref import DefaultConnectionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .site_connection_ref import SiteConnectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransferRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transferRefs_RelStructure"

    connection_ref_or_transfer_ref: list[Union[DefaultConnectionRef, SiteConnectionRef, ConnectionRef, AccessRef]] = field(
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
        },
    )
