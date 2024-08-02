from dataclasses import dataclass, field

from .call_status_enumeration import CallStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ArrivalStatus:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: CallStatusEnumeration = field(
        metadata={
            "required": True,
        }
    )
