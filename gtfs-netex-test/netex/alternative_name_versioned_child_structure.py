from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .name_type_enumeration import NameTypeEnumeration
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AlternativeNameVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AlternativeName_VersionedChildStructure"

    named_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "NamedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_type: Optional[NameTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "NameType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: MultilingualString = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    abbreviation: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualifier_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "QualifierName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
