from dataclasses import dataclass, field
from netex.type_of_security_list_version_structure import TypeOfSecurityListVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfSecurityList(TypeOfSecurityListVersionStructure):
    """A classification of SECURITY LIST.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
