from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FilterByMonitoringRef:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        init=False,
        default=True,
        metadata={
            "required": True,
        },
    )
