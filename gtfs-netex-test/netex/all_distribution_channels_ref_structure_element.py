from dataclasses import dataclass, field
from .type_of_value_ref_structure import TypeOfValueRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllDistributionChannelsRefStructureElement(TypeOfValueRefStructure):
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: RestrictedVar
