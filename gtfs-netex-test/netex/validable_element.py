from dataclasses import dataclass, field
from netex.validable_element_version_structure import ValidableElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidableElement(ValidableElementVersionStructure):
    """
    A sequence or set of FARE STRUCTURE ELEMENTs, grouped together to be validated
    in one go.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
