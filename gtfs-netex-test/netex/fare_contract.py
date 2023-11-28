from dataclasses import dataclass, field
from netex.fare_contract_version_structure import FareContractVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContract(FareContractVersionStructure):
    """A contract with a particular (but possibly anonymous) customer, ruling the
    consumption of transport services (and joint services).

    A FARE CONTRACT may be designed for a fixed SALES OFFER PACKAGE
    (e.g. ticket) or to allow successive purchases of SALES OFFER
    PACKAGEs.

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
