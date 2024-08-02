from dataclasses import dataclass, field

from .interchange_status_enumeration import InterchangeStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InterchangeStatusType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: InterchangeStatusEnumeration = field(
        default=InterchangeStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
