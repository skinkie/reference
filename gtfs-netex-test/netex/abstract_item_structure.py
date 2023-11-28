from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractItemStructure:
    """
    Type for an Activity.

    :ivar recorded_at_time: Time at which data was recorded.
    """
    recorded_at_time: XmlDateTime = field(
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
