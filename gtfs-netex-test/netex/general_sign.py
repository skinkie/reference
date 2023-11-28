from dataclasses import dataclass, field
from netex.general_sign_structure import GeneralSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralSign(GeneralSignStructure):
    """
    Specialisation of SIGN EQUIPMENT sor signs which are not HEADING SIGNs nor
    PLACE SIGNs.

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
