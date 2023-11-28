from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from netex.containment_enumeration import ContainmentEnumeration
from netex.mandatory_enumeration import MandatoryEnumeration
from netex.modification_set_enumeration import ModificationSetEnumeration
from netex.relationship_ref import RelationshipRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassRelationshipInFrameStructure:
    """
    Type for Relationship of Class of Entity.

    :ivar relationship_ref:
    :ivar mandatory: Whether relationship is required, optional or not
        allowed.
    :ivar containment: Whether reference elements can be inline or by
        reference.  This is constrained by schema usage.
    :ivar modification_set: Whether contained elements must be whole set
        or can be just a Delta.
    :ivar name: Name of attribute in CLASS IN REPOSITORY.
    """
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
        }
    )
    containment: Optional[ContainmentEnumeration] = field(
        default=None,
        metadata={
            "name": "Containment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modification_set: Optional[ModificationSetEnumeration] = field(
        default=None,
        metadata={
            "name": "ModificationSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
