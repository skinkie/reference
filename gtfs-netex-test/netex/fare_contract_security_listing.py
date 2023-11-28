from dataclasses import dataclass, field
from netex.fare_contract_security_listing_versioned_child_structure import FareContractSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractSecurityListing(FareContractSecurityListingVersionedChildStructure):
    """
    A listing of a FARE CONTRACT on a SECURITY LIST.

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
