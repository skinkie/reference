from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from netex.mandatory_enumeration import MandatoryEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassAttributeInFrameStructure:
    """
    Type for Attribute of Class of Entity.

    :ivar type_value: Class of attribute.
    :ivar mandatory: Whether element is required, optional or not
        allowed.
    :ivar name: Name of attribute in CLASS IN REPOSITORY.
    """
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Type",
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
    name: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
