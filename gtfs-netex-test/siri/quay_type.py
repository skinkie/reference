from dataclasses import dataclass, field

from .type_of_nested_quay_enumeration import TypeOfNestedQuayEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class QuayType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TypeOfNestedQuayEnumeration = field(
        metadata={
            "required": True,
        }
    )
