from dataclasses import dataclass, field
from netex.abstract_item_structure import AbstractItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractRequiredIdentifiedItemStructure(AbstractItemStructure):
    """
    Type for an Activity that can be referenced.

    :ivar item_identifier: Identifier of item.
    """
    item_identifier: str = field(
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
