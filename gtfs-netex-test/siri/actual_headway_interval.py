from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ActualHeadwayInterval:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: XmlDuration = field(
        metadata={
            "required": True,
        }
    )
