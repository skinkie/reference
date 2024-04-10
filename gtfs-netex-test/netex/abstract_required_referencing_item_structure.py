from dataclasses import dataclass, field

from .abstract_item_structure import AbstractItemStructure
from .item_ref_structure import ItemRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractRequiredReferencingItemStructure(AbstractItemStructure):
    item_ref: ItemRefStructure = field(
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
