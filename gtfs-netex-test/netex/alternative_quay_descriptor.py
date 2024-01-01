from dataclasses import dataclass, field
from .alternative_quay_descriptor_versioned_child_structure import (
    AlternativeQuayDescriptorVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeQuayDescriptor(
    AlternativeQuayDescriptorVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    type_of_name: str = field(
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "required": True,
        }
    )
    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
    name_type: RestrictedVar
