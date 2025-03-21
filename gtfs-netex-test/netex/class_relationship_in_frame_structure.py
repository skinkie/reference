from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .containment_enumeration import ContainmentEnumeration
from .mandatory_enumeration import MandatoryEnumeration
from .modification_set_enumeration import ModificationSetEnumeration
from .relationship_ref import RelationshipRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClassRelationshipInFrameStructure:
    relationship_ref: RelationshipRef = field(
        metadata={
            "name": "RelationshipRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    mandatory: Optional[MandatoryEnumeration] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    containment: Optional[ContainmentEnumeration] = field(
        default=None,
        metadata={
            "name": "Containment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    modification_set: Optional[ModificationSetEnumeration] = field(
        default=None,
        metadata={
            "name": "ModificationSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
