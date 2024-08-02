from dataclasses import dataclass, field
from typing import List, Optional

from .affects_scope_structure import AffectsScopeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .scope_type_enumeration import ScopeTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ActionDataStructure:
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    prompt: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Prompt",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_at_scope: Optional["ActionDataStructure.PublishAtScope"] = field(
        default=None,
        metadata={
            "name": "PublishAtScope",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class PublishAtScope:
        scope_type: ScopeTypeEnumeration = field(
            metadata={
                "name": "ScopeType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        affects: AffectsScopeStructure = field(
            metadata={
                "name": "Affects",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
