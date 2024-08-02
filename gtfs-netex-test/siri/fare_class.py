from dataclasses import dataclass, field

from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FareClass:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FareClassEnumeration = field(
        default=FareClassEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
