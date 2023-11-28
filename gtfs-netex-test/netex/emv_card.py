from dataclasses import dataclass, field
from netex.emv_card_version_structure import EmvCardVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EmvCard(EmvCardVersionStructure):
    """
    A standardised payment card (Europay MasterCard Visa etc) , capable of being
    used as token for an ABT system +v1.2.2.

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
