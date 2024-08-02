from dataclasses import dataclass, field

from .service_condition_enumeration import ServiceConditionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Condition:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ServiceConditionEnumeration = field(
        metadata={
            "required": True,
        }
    )
