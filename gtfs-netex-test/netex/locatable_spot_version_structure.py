from dataclasses import dataclass, field
from typing import Optional

from .equipable_space_version_structure import EquipableSpaceVersionStructure
from .sensors_in_spot_rel_structure import SensorsInSpotRelStructure
from .spot_column_ref import SpotColumnRef
from .spot_row_ref import SpotRowRef
from .type_of_locatable_spot_ref import TypeOfLocatableSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocatableSpotVersionStructure(EquipableSpaceVersionStructure):
    class Meta:
        name = "LocatableSpot_VersionStructure"

    type_of_locatable_spot_ref: Optional[TypeOfLocatableSpotRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLocatableSpotRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_row_ref: Optional[SpotRowRef] = field(
        default=None,
        metadata={
            "name": "SpotRowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spot_column_ref: Optional[SpotColumnRef] = field(
        default=None,
        metadata={
            "name": "SpotColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sensors_in_spot: Optional[SensorsInSpotRelStructure] = field(
        default=None,
        metadata={
            "name": "sensorsInSpot",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
