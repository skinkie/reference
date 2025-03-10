from dataclasses import dataclass, field
from typing import Optional

from .class_attribute_in_frame import ClassAttributeInFrame
from .class_ref_type_enumeration import ClassRefTypeEnumeration
from .class_relationship_in_frame import ClassRelationshipInFrame
from .mandatory_enumeration import MandatoryEnumeration
from .type_of_frame_ref import TypeOfFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClassInFrameStructure:
    class_ref_type: Optional[ClassRefTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mandatory: Optional[MandatoryEnumeration] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    attributes: Optional["ClassInFrameStructure.Attributes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relationships: Optional["ClassInFrameStructure.Relationships"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )

    @dataclass(slots=True, kw_only=True)
    class Attributes:
        class_attribute_in_frame: list[ClassAttributeInFrame] = field(
            default_factory=list,
            metadata={
                "name": "ClassAttributeInFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True, kw_only=True)
    class Relationships:
        class_relationship_in_frame: list[ClassRelationshipInFrame] = field(
            default_factory=list,
            metadata={
                "name": "ClassRelationshipInFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
