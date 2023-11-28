from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractRequestStructure:
    """
    Type for General SIRI Request.
    """
    request_timestamp: XmlDateTime = field(
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
