from dataclasses import dataclass, field
from netex.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SelfDriveSubmode:
    """TPEG pti12 SelfDrive submodes.

    (NB Use  SimpleVehicleType / Vehicle Category to describe specific
    type)
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SelfDriveSubmodeEnumeration = field(
        default=SelfDriveSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
