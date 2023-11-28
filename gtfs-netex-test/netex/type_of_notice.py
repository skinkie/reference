from dataclasses import dataclass, field
from netex.type_of_notice_value_structure import TypeOfNoticeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfNotice(TypeOfNoticeValueStructure):
    """
    A classification of a NOTICE according to its functional purpose.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
