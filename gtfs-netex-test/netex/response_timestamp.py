from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponseTimestamp:
    """
    Time individual response element was created.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )
