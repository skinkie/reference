from dataclasses import dataclass, field
from typing import Optional

from .installed_equipment_version_structure import InstalledEquipmentVersionStructure
from .sensor_communications_enumeration import SensorCommunicationsEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SensorEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "SensorEquipment_VersionStructure"

    communication_method: Optional[SensorCommunicationsEnumeration] = field(
        default=None,
        metadata={
            "name": "CommunicationMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
