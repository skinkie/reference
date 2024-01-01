from dataclasses import dataclass, field


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class IncludeTranslations:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
