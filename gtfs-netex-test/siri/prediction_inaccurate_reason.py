from dataclasses import dataclass, field

from .prediction_inaccurate_reason_enumeration import PredictionInaccurateReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PredictionInaccurateReason:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PredictionInaccurateReasonEnumeration = field(
        metadata={
            "required": True,
        }
    )
