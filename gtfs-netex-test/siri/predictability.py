from dataclasses import dataclass, field

from .predictability_enumeration import PredictabilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Predictability:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PredictabilityEnumeration = field()
