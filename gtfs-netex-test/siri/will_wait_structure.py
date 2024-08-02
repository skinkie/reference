from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class WillWaitStructure:
    wait_until_time: XmlDateTime = field(
        metadata={
            "name": "WaitUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    driver_has_acknowledge_will_wait_or_driver_has_acknowledged_will_wait: Optional[Union["WillWaitStructure.DriverHasAcknowledgeWillWait", "WillWaitStructure.DriverHasAcknowledgedWillWait"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DriverHasAcknowledgeWIllWait",
                    "type": ForwardRef("WillWaitStructure.DriverHasAcknowledgeWillWait"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DriverHasAcknowledgedWillWait",
                    "type": ForwardRef("WillWaitStructure.DriverHasAcknowledgedWillWait"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class DriverHasAcknowledgeWillWait:
        value: bool = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DriverHasAcknowledgedWillWait:
        value: bool = field(
            metadata={
                "required": True,
            }
        )
