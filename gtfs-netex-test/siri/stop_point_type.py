from dataclasses import dataclass, field

from .stop_point_type_enumeration import StopPointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopPointType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: StopPointTypeEnumeration = field(
        default=StopPointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
