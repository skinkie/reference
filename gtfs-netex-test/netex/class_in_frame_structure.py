from dataclasses import dataclass, field
from typing import List, Optional
from netex.class_attribute_in_frame import ClassAttributeInFrame
from netex.class_ref_type_enumeration import ClassRefTypeEnumeration
from netex.class_relationship_in_frame import ClassRelationshipInFrame
from netex.mandatory_enumeration import MandatoryEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassInFrameStructure:
    """
    Type for CLASS IN FRAME.

    :ivar class_ref_type: Nature of reference: Members | Member
        References | All.
    :ivar type_of_frame_ref: Type of FrAMe containing CLass.
    :ivar mandatory: Whether element is required, optional or not
        allowed.
    :ivar attributes: Requirements for attributes in class.
    :ivar relationships: Requirements for attributes in class.
    :ivar name_of_class: Name of ENTITY CLASS i.e. TYPE.
    """
    class_ref_type: Optional[ClassRefTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ClassRefType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mandatory: Optional[MandatoryEnumeration] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    attributes: Optional["ClassInFrameStructure.Attributes"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relationships: Optional["ClassInFrameStructure.Relationships"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Attributes:
        """
        :ivar class_attribute_in_frame: Attribute of Class of ENTITY.
            This is a metaclass that allows services to specify whether
            an attribute for a class must be present in a given frame.
        """
        class_attribute_in_frame: List[ClassAttributeInFrame] = field(
            default_factory=list,
            metadata={
                "name": "ClassAttributeInFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Relationships:
        """
        :ivar class_relationship_in_frame: Attribute of Class of ENTITY.
            This is a metaclass that allows services to specify whether
            an attribute for a class must be present in a given frame.
        """
        class_relationship_in_frame: List[ClassRelationshipInFrame] = field(
            default_factory=list,
            metadata={
                "name": "ClassRelationshipInFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            }
        )
