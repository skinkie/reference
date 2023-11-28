from dataclasses import dataclass
from netex.transfer_restriction_ref_structure import TransferRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferRestrictionRef(TransferRestrictionRefStructure):
    """
    Reference to a TRANSFER RESTRICTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
