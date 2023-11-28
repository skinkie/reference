from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionOfObjectRefStructure:
    """
    Type for a versioned reference to a NeTEx Object.

    :ivar value:
    :ivar name_of_ref_class: Name of Class of the referenced entity.
        Allows reflection. Fixed for each entity type.
    :ivar created: Date reference was first created.
    :ivar changed: Date reference was last changed.
    :ivar version: Version number of referenced entity.
    :ivar modification: Nature of last modification: new, revise,
        delete, unchanged;
    :ivar ref: Identifier of referenced entity.
    :ivar version_ref: Identifier of version of referenced entity. For
        use when reference is External and a specific version is
        required. Mutually exclusive with version
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    name_of_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        }
    )
