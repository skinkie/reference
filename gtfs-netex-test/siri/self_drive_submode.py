from dataclasses import dataclass, field

from .self_drive_submodes_of_transport_enumeration import SelfDriveSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SelfDriveSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SelfDriveSubmodesOfTransportEnumeration = field(
        default=SelfDriveSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
