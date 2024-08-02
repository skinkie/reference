from dataclasses import dataclass, field

from .alert_cause_enumeration import AlertCauseEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AlertCause:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AlertCauseEnumeration = field(
        metadata={
            "required": True,
        }
    )
