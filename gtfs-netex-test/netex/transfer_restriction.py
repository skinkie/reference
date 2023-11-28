from dataclasses import dataclass, field
from netex.transfer_restriction_version_structure import TransferRestrictionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferRestriction(TransferRestrictionVersionStructure):
    """
    A CONSTRAINT that can be applied on a CONNECTION or INTERCHANGE between two
    SCHEDULED STOP POINT, preventing or forbidding the passenger to use it.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
