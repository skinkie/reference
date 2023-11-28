from dataclasses import dataclass, field
from typing import Optional
from netex.connection_end_structure import ConnectionEndStructure
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectionVersionStructure(TransferVersionStructure):
    """
    Type for a CONNECTION link restricts id.

    :ivar external_connection_link_ref: An alternative  code that
        uniquely identifies the CONNECTION link Specifically for use in
        AVMS systems that require an alias, if. For VDV compatibility.
    :ivar from_value: Origin end of CONNECTION.
    :ivar to: Destination end of  CONNECTION.
    :ivar transfer_only: Whether  connecting at this stop passengers may
        only transfer. If true, then they may not enter or exit at the
        station.
    """
    class Meta:
        name = "Connection_VersionStructure"

    external_connection_link_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_value: Optional[ConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to: Optional[ConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransferOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
