from dataclasses import dataclass, field
from typing import Optional
from netex.installed_equipment_version_structure import InstalledEquipmentVersionStructure
from netex.locking_mechanism_enumeration import LockingMechanismEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleReleaseEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    """
    Type for a VEHICLE RELEASE EQUIPMENT.

    :ivar remote_control: whether shelter is enclosed.
    :ivar local_control: Whether reservation is required.
    :ivar locking_mechanism: Type of locking mechnaism.
    """
    class Meta:
        name = "VehicleReleaseEquipment_VersionStructure"

    remote_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RemoteControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LocalControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locking_mechanism: Optional[LockingMechanismEnumeration] = field(
        default=None,
        metadata={
            "name": "LockingMechanism",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
