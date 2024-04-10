from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RequestTimestamp:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )
