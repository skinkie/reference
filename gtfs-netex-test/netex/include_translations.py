from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class IncludeTranslations:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
