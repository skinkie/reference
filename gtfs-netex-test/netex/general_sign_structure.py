from dataclasses import dataclass, field
from typing import Optional
from netex.multilingual_string import MultilingualString
from netex.sign_content_enumeration import SignContentEnumeration
from netex.sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralSignStructure(SignEquipmentVersionStructure):
    """
    Type for an GENERAL SIGN.

    :ivar content: Content of Sign.
    :ivar sign_content_type: Classification of content as standard
        category.
    """
    content: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sign_content_type: Optional[SignContentEnumeration] = field(
        default=None,
        metadata={
            "name": "SignContentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
