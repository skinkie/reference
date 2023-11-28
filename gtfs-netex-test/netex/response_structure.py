from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponseStructure:
    """
    General Type for General SIRI Response.
    """
    response_timestamp: XmlDateTime = field(
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
