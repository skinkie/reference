from dataclasses import dataclass, field
from .abstract_item_structure import AbstractItemStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequiredIdentifiedItemStructure(AbstractItemStructure):
    item_identifier: str = field(
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
