from dataclasses import dataclass, field
from netex.blacklist_version_structure import BlacklistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Blacklist(BlacklistVersionStructure):
    """
    A list of items (TRAVEL DOCUMENTs,  CONTRACTs etc) the validity of which has
    been cancelled temporarily or permanently, for a specific reason like loss of
    the document, technical malfunction, no credit on bank account, offences
    committed by the customer, etc.

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
