from dataclasses import dataclass, field
from .class_ref_structure import ClassRefStructure
from .class_ref_type_enumeration import ClassRefTypeEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassInFrameRefStructure(ClassRefStructure):
    class_ref_type: ClassRefTypeEnumeration = field(
        default=ClassRefTypeEnumeration.MEMBERS,
        metadata={
            "name": "classRefType",
            "type": "Attribute",
        },
    )
