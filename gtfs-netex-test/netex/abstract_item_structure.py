from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractItemStructure:
    recorded_at_time: XmlDateTime = field(
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
