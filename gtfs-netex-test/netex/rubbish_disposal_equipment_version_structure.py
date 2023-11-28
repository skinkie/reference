from dataclasses import dataclass, field
from typing import Optional
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RubbishDisposalEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for RUBBISH DISPOSAL EQUIPMENT.

    :ivar sharps_disposal: Whether there are disposal facilities for
        needles or medical sharps.
    :ivar recycling: Whether there is separation for recycling.
    """
    class Meta:
        name = "RubbishDisposalEquipment_VersionStructure"

    sharps_disposal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    recycling: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Recycling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
