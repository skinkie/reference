from dataclasses import dataclass, field
from typing import List, Optional
from netex.description_reference import DescriptionReference
from netex.identifier import Identifier
from netex.name import Name

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"

    description_reference: Optional[DescriptionReference] = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
