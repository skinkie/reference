from dataclasses import dataclass, field
from typing import Optional
from .abstract_item_structure import AbstractItemStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractReferencingItemStructure(AbstractItemStructure):
    item_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
