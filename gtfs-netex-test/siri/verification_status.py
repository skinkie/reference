from dataclasses import dataclass, field

from .verification_status_enumeration import VerificationStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VerificationStatus:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: VerificationStatusEnumeration = field()
