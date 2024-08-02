from dataclasses import dataclass, field

from .severity_enumeration import SeverityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Severity:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SeverityEnumeration = field(
        default=SeverityEnumeration.NORMAL,
        metadata={
            "required": True,
        },
    )
