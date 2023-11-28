from dataclasses import dataclass, field
from netex.accountable_element_structure import AccountableElementStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccountableElement(AccountableElementStructure):
    """A period of a driver's DUTY during which (s)he is continuously working
    without a BREAK.

    PAUSEs during which (the)he remains responsible for the vehicle may
    be included.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
