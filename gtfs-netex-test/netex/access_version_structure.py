from dataclasses import dataclass, field
from netex.access_end_structure import AccessEndStructure
from netex.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessVersionStructure(TransferVersionStructure):
    """
    Type for an ACCESS link.

    :ivar from_value: Origin end of ACCESS link.
    :ivar to: Destination end of ACCESS link.
    """
    class Meta:
        name = "Access_VersionStructure"

    from_value: AccessEndStructure = field(
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to: AccessEndStructure = field(
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
